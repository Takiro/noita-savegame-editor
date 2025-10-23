from defusedxml import ElementTree as ET
from xml.etree.ElementTree import ElementTree, Element
from math import floor

from typing import Tuple


def cap(number, min_, max_):
    """Cap a value between a lower and/or upper bound (inclusive)"""
    if min_ is not None and number < min_:
        return min_
    if max_ is not None and number > max_:
        return max_
    return number


def _str_to_bool(s):
    return s != "0"


def _bool_to_str(b):
    return "1" if b else "0"


class Card:
    def __init__(self, xml_element):
        self._card = xml_element

        self._item_action = self._card.find("ItemActionComponent")
        self._card_item_component = self._card.find("ItemComponent")

    def get_action_id(self):
        """The type of card/spell"""
        return self._item_action.get('action_id')

    @property
    def permanently_attached(self):
        """On wands cards (spells) can be permanently attached. They consume no slot and are always cast on use."""
        return _str_to_bool(self._card_item_component.get("permanently_attached"))

    @permanently_attached.setter
    def permanently_attached(self, is_attached):
        self._card_item_component.set("permanently_attached", _bool_to_str(is_attached))

    @property
    def uses_remaining(self):
        return int(self._card_item_component.get("uses_remaining"))

    @uses_remaining.setter
    def uses_remaining(self, uses):
        uses = cap(uses, -1, None)
        self._card_item_component.set("uses_remaining", str(uses))

    @property
    def inventory_slot(self) -> Tuple[int, int]:
        x = self._card_item_component.get("inventory_slot.x")
        y = self._card_item_component.get("inventory_slot.y")

        return int(x), int(y)

    @inventory_slot.setter
    def inventory_slot(self, slot: Tuple[int, int]):
        # TODO set cap to actual inventory size
        x = cap(slot[0], 0, 15)
        y = cap(slot[1], 0, 15)
        self._card_item_component.set("inventory_slot.x", str(x))
        self._card_item_component.set("inventory_slot.y", str(y))


class Wand:
    def __init__(self, xml_element):
        self._wand = xml_element
        self._abilities = self._wand.find("AbilityComponent")
        self._gun_config = self._abilities.find("gun_config")
        self._gun_action_config = self._abilities.find("gunaction_config")

        # this prevents the Wands to be stuck in cooldown after importing an old savegame
        # because the games saves the frame count to determine when it can fire again
        self._abilities.set("mCastDelayStartFrame", "0")
        self._abilities.set("mNextFrameUsable", "0")
        self._abilities.set("mReloadFramesLeft", "0")
        self._abilities.set("mReloadNextFrameUsable", "0")

        self.cards = []

        cards = self._wand.findall("Entity[@tags='card_action']")
        for c in cards:
            self.cards.append(Card(c))

    def get_name(self):
        return self._abilities.get("ui_name")

    @property
    def mana(self):
        return float(self._abilities.get("mana"))

    @mana.setter
    def mana(self, mana):
        self._abilities.set("mana", str(mana))

    @property
    def mana_recharge(self):
        return float(self._abilities.get("mana_charge_speed"))

    @mana_recharge.setter
    def mana_recharge(self, mana_recharge):
        self._abilities.set("mana_charge_speed", str(mana_recharge))

    @property
    def mana_max(self):
        return float(self._abilities.get("mana_max"))

    @mana_max.setter
    def mana_max(self, mana_max):
        self._abilities.set("mana_max", str(mana_max))

    @property
    def spells_cast(self):
        """The number of spells cast simultaneously per shot."""
        return int(self._gun_config.get("actions_per_round"))

    @spells_cast.setter
    def spells_cast(self, spells_cast):
        self._gun_config.set("actions_per_round", str(spells_cast))

    @property
    def capacity(self):
        return int(self._gun_config.get("deck_capacity"))

    @capacity.setter
    def capacity(self, capacity):
        """Set the number of slots a Wand has. Capped at 30."""
        # not sure if the game has a hard cap of slots for a wand but 28 is the biggest seen so far,
        # anything bigger than 30 would be hard to display in the game anyway
        capacity = cap(capacity, 0, 30)
        self._gun_config.set("deck_capacity", str(capacity))

    @property
    def reload_time(self):
        return float(self._gun_config.get("reload_time"))

    @reload_time.setter
    def reload_time(self, reload_time):
        reload_time = cap(reload_time, 0, None)
        self._gun_config.set("reload_time", str(reload_time))

    @property
    def cast_delay(self):
        return float(self._gun_action_config.get("fire_rate_wait"))

    @cast_delay.setter
    def cast_delay(self, cast_delay):
        cast_delay = cap(cast_delay, 0, None)
        self._gun_action_config.set("fire_rate_wait", str(cast_delay))

    @property
    def shuffles(self):
        return _str_to_bool(self._gun_config.get("shuffle_deck_when_empty"))

    @shuffles.setter
    def shuffles(self, shuffles):
        self._gun_config.set("shuffle_deck_when_empty", _bool_to_str(shuffles))

    @property
    def spread_degrees(self):
        """Sets/gets the spread in degrees ranging from 0 to 180"""
        return float(self._gun_action_config.get("spread_degrees"))

    @spread_degrees.setter
    def spread_degrees(self, degrees):
        # I assume 180 is max, I never tested what the maximum is but with a
        # spread higher than that, actually hitting something can be impossible.
        # 180° is already insane.
        degrees = cap(degrees, 0, 180)
        self._gun_action_config.set("spread_degrees", str(degrees))


class SaveGame:
    def __init__(self):
        self._quick_inventory = None
        self.inventory = []
        self._full_inventory = None
        self._wallet = None
        self._damage_model = None
        self._inventory_component = None
        self._character_data = None
        self._element_tree = None
        self._root = None
        self.wands = []

    def load(self, file_path):
        self._element_tree = ET.parse(file_path)
        self._root = self._element_tree.getroot()
        self._character_data = self._root.find("CharacterDataComponent")
        self._inventory_component = self._root.find("Inventory2Component")
        # full_inventory_slots = (
        #    inventory_component.get("full_inventory_slots_x"), inventory_component.get("full_inventory_slots_y"))
        self._damage_model = self._root.find("DamageModelComponent")
        self._wallet = self._root.find("WalletComponent")
        self._load_inventory()

    def _load_inventory(self):
        self._quick_inventory = self._root.find("Entity[@name='inventory_quick']")
        self.wands.clear()
        wands = self._quick_inventory.iterfind("Entity")

        for wand in wands:
            tags = wand.get("tags").split(",")
            if "wand" not in tags:
                continue
            w = Wand(wand)
            self.wands.append(w)

        self._full_inventory = self._root.find("Entity[@name='inventory_full']")
        cards = self._full_inventory.findall("Entity[@tags='card_action']")

        self.inventory.clear()
        for c in cards:
            self.inventory.append(Card(c))

    @property
    def flying_needs_recharge(self):
        return self._character_data.get("flying_needs_recharge") == "1"

    @flying_needs_recharge.setter
    def flying_needs_recharge(self, b):
        self._character_data.set("flying_needs_recharge", _bool_to_str(b))

    @property
    def inventory_bars(self):
        """Sets/Gets the number of bars of the full inventory as a number between 1 and 16 (inclusive)
        if value is outside the range it gets capped at min/maximum."""
        return int(self._inventory_component.get("full_inventory_slots_y"))

    @inventory_bars.setter
    def inventory_bars(self, number_of_bars):
        number_of_bars = cap(number_of_bars, 1, 16)
        self._inventory_component.set("full_inventory_slots_y", str(number_of_bars))

    @property
    def air_needed(self):
        """If set to true, player does not run out of air when underwater."""
        return _str_to_bool(self._damage_model.get("air_needed"))

    @air_needed.setter
    def air_needed(self, b):
        self._damage_model.set("air_needed", _bool_to_str(b))

    @property
    def current_health(self):
        hp = self._damage_model.get("hp")
        return self._float_to_health(float(hp))

    @current_health.setter
    def current_health(self, health):
        hp = self._health_to_float(health)
        self._damage_model.set("hp", str(hp))

    @property
    def max_health(self):
        hp = self._damage_model.get("max_hp")
        return self._float_to_health(float(hp))

    @max_health.setter
    def max_health(self, health):
        hp = self._health_to_float(health)
        self._damage_model.set("max_hp", str(hp))

    @property
    def health_cap(self):
        hp = self._damage_model.get("max_hp_cap")
        return self._float_to_health(float(hp))

    @health_cap.setter
    def health_cap(self, health):
        hp = self._health_to_float(health)
        self._damage_model.set("max_hp_cap", str(hp))

    @property
    def money(self):
        return int(self._wallet.get("money"))

    @money.setter
    def money(self, money):
        if money < 0:
            money = 0
        self._wallet.set("money", str(money))

    def save(self, file_path):
        self._element_tree.write(file_path)

    def clone_card(self, card):
        """Todo: implement inventory management, maybe"""
        pass

    def heal(self):
        """Sets the health to its current maximum"""
        self._damage_model.set("hp", self._damage_model.get("max_hp"))

    def export_inventory(self, file):
        """Exports the contents and the size of the current inventory."""
        root = Element("inventory")
        root.set("inventory_slots_x", self._inventory_component.get("full_inventory_slots_x"))
        root.set("inventory_slots_y", self._inventory_component.get("full_inventory_slots_y"))
        root.append(self._full_inventory)
        root.append(self._quick_inventory)

        inventory_tree = ElementTree(root)
        inventory_tree.write(file)

    def import_inventory(self, file):
        """Imports a previously exported inventory and sets the size accordingly."""
        tree: ElementTree = ET.parse(file)
        root = tree.getroot()
        size_x = root.get("inventory_slots_x")
        size_y = root.get("inventory_slots_y")

        imported_full_inventory = root.find("Entity[@name='inventory_full']")
        imported_quick_inventory = root.find("Entity[@name='inventory_quick']")

        self._root.remove(self._full_inventory)
        self._root.remove(self._quick_inventory)
        self._root.append(imported_quick_inventory)
        self._root.append(imported_full_inventory)

        self._load_inventory()

        self._inventory_component.set("full_inventory_slots_x", size_x)
        self._inventory_component.set("full_inventory_slots_y", size_y)

    def update_spell_library(self):
        pass

    @staticmethod
    def _float_to_health(f):
        """Converts the game's multiplier notation to the actual value as seen on the health bar"""
        return floor(f * 25)

    @staticmethod
    def _health_to_float(i):
        """Converts the value to the game's multiplier notation."""
        return i / 25.0


def print_stuff(save):
    print("Flying nees recharge:", save.flying_needs_recharge)
    print("Number of inventory bars:", save.inventory_bars)
    print("Air needed:", save.air_needed)
    print("Money:", save.money)
    print(f"Health: {save.current_health} of {save.max_health}")
    print("Health cap:", save.health_cap)
    print()
    print("Wands")
    for wand in save.wands:
        print(wand.get_name())
        print(f"Mana {wand.mana} of {wand.mana_max}")
        print("Mana recharge:", wand.mana_recharge)
        print("Shuffles:", wand.shuffles)
        print("Spread:", wand.spread_degrees)
        print("Spells cast:", wand.spells_cast)
        print("Capacity", wand.capacity)
        print("Reload", wand.reload_time)
        print("Cards:")
        for card in wand.cards:
            ammo = card.uses_remaining
            perm = card.permanently_attached
            print(card.inventory_slot, card.get_action_id(), "Permanent" if perm else "", ammo if ammo != -1 else "")
        print()

    print("Inventory")
    for card in save.inventory:
        ammo = card.uses_remaining
        print(card.inventory_slot, card.get_action_id(), ammo if ammo != -1 else "")