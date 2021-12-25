import sys

from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog, QLabel
from sys import argv
from ui_main_window import Ui_MainWindow
from savegame import SaveGame, Wand
from os import path
import platform


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self._savegame = None
        self._connect_signals()
        self._current_save_file_path = ""
        # TODO: Check where the savegame is on Linux
        self._search_path = path.abspath(path.expandvars("%appdata%/../LocalLow/Nolla_Games_Noita/save00/"))

    def _connect_signals(self):
        self.action_quick_load.triggered.connect(self._quick_load_savegame)
        self.action_open.triggered.connect(self._open_file)
        self.action_save.triggered.connect(self._save_file)
        self.action_export_inventory.triggered.connect(self._export)
        self.action_import_inventory.triggered.connect(self._import)
        self.action_quit.triggered.connect(lambda: sys.exit())

        self.unlimited_flight_check.toggled.connect(lambda x: self._change_label_on_off(self.unlimited_flight_check, x))
        self.unlimited_breath_check.toggled.connect(lambda x: self._change_label_on_off(self.unlimited_breath_check, x))
        self.wand_1_shuffle_check.toggled.connect(lambda x: self._change_label_yes_no(self.wand_1_shuffle_check, x))
        self.wand_2_shuffle_check.toggled.connect(lambda x: self._change_label_yes_no(self.wand_2_shuffle_check, x))
        self.wand_3_shuffle_check.toggled.connect(lambda x: self._change_label_yes_no(self.wand_3_shuffle_check, x))
        self.wand_4_shuffle_check.toggled.connect(lambda x: self._change_label_yes_no(self.wand_4_shuffle_check, x))
        self.inventory_bars_edit.valueChanged.connect(lambda x: self.inventory_use_label.setText(str(x*16)))

    @property
    def current_save_file_path(self):
        return self._current_save_file_path

    @current_save_file_path.setter
    def current_save_file_path(self, save_file_path):
        self._current_save_file_path = save_file_path
        self.setWindowTitle(f"Noita Save-Editor {save_file_path}")


    @property
    def savegame(self):
        return self._savegame

    @savegame.setter
    def savegame(self, savegame):
        self._savegame = savegame
        self.action_save.setEnabled(savegame is not None)
        self.action_export_inventory.setEnabled(savegame is not None)
        self.action_import_inventory.setEnabled(savegame is not None)

    def _export(self):
        file_path = QFileDialog.getSaveFileName(self, "Save inventory file", path.expanduser("~"), "XML(*.xml)")
        if file_path[0]:
            self.savegame.export_inventory(file_path[0])

    def _import(self):
        file_path = QFileDialog.getOpenFileName(self, "Open inventory file", path.expanduser("~"), "XML(*.xml)")
        if file_path[0]:
            self.savegame.import_inventory(file_path[0])
            self._fill_form()

    def _save_file(self):

        self.savegame.current_health = self.health_edit.value()
        self.savegame.max_health = self.max_health_edit.value()
        self.savegame.health_cap = self.health_cap_edit.value()
        self.savegame.flying_needs_recharge = not self.unlimited_flight_check.isChecked()
        self.savegame.air_needed = not self.unlimited_breath_check.isChecked()
        self.savegame.money = self.money_edit.value()
        # ToDo: show a warning and do something when inventory is too small
        self.savegame.inventory_bars = self.inventory_bars_edit.value()

        try:
            wand_1: Wand = self.savegame.wands[0]
            wand_1.mana = self.wand_1_mana_edit.value()
            wand_1.mana_max = self.wand_1_max_mana_edit.value()
            wand_1.mana_recharge = self.wand_1_mana_recharge_edit.value()
            wand_1.shuffles = self.wand_1_shuffle_check.isChecked()
            wand_1.spread_degrees = self.wand_1_spread_edit.value()
            wand_1.capacity = self.wand_1_capacity_edit.value()
            wand_1.spells_cast = self.wand_1_spells_cast_edit.value()
            wand_1.reload_time = self.wand_1_reload_time_edit.value()
            # TODO make spells editable and write them to the xml
        except IndexError:
            pass

        try:
            wand_2: Wand = self.savegame.wands[1]
            wand_2.mana = self.wand_2_mana_edit.value()
            wand_2.mana_max = self.wand_2_max_mana_edit.value()
            wand_2.mana_recharge = self.wand_2_mana_recharge_edit.value()
            wand_2.shuffles = self.wand_2_shuffle_check.isChecked()
            wand_2.spread_degrees = self.wand_2_spread_edit.value()
            wand_2.capacity = self.wand_2_capacity_edit.value()
            wand_2.spells_cast = self.wand_2_spells_cast_edit.value()
            wand_2.reload_time = self.wand_2_reload_time_edit.value()
            # TODO make spells editable and write them to the xml
        except IndexError:
            pass

        try:
            wand_3: Wand = self.savegame.wands[2]
            wand_3.mana = self.wand_3_mana_edit.value()
            wand_3.mana_max = self.wand_3_max_mana_edit.value()
            wand_3.mana_recharge = self.wand_3_mana_recharge_edit.value()
            wand_3.shuffles = self.wand_3_shuffle_check.isChecked()
            wand_3.spread_degrees = self.wand_3_spread_edit.value()
            wand_3.capacity = self.wand_3_capacity_edit.value()
            wand_3.spells_cast = self.wand_3_spells_cast_edit.value()
            wand_3.reload_time = self.wand_3_reload_time_edit.value()
            # TODO make spells editable and write them to the xml
        except IndexError:
            pass

        try:
            wand_4: Wand = self.savegame.wands[3]
            wand_4.mana = self.wand_4_mana_edit.value()
            wand_4.mana_max = self.wand_4_max_mana_edit.value()
            wand_4.mana_recharge = self.wand_4_mana_recharge_edit.value()
            wand_4.shuffles = self.wand_4_shuffle_check.isChecked()
            wand_4.spread_degrees = self.wand_4_spread_edit.value()
            wand_4.capacity = self.wand_4_capacity_edit.value()
            wand_4.spells_cast = self.wand_4_spells_cast_edit.value()
            wand_4.reload_time = self.wand_4_reload_time_edit.value()
            # TODO make spells editable and write them to the xml
        except IndexError:
            pass

        #ToDo: make inventory editable and export it

        self.savegame.save(self.current_save_file_path)

    @staticmethod
    def _change_label_yes_no(source, state):
        source.setText("yes" if state else "no")

    @staticmethod
    def _change_label_on_off(source, state):
        source.setText("on" if state else "off")

    def _open_file(self):
        search_path = path.expanduser("~")
        if platform.system() == "Windows":
            if path.exists(self._search_path):
                search_path = self._search_path

        file_path = QFileDialog.getOpenFileName(self, "Open savegame", search_path, "XML(*.xml)")
        if file_path[0]:
            self._load_savegame(file_path[0])

    def _quick_load_savegame(self):
        try:
            file_path = path.join(self._search_path, 'player.xml')
            self._load_savegame(file_path)
        except FileNotFoundError:
            pass

    def _load_savegame(self, file_path):

        self.current_save_file_path = file_path
        savegame = SaveGame()
        savegame.load(file_path)
        self.savegame = savegame
        self._fill_form()

    def _fill_form(self):
        self.health_edit.setValue(self.savegame.current_health)
        self.max_health_edit.setValue(self.savegame.max_health)
        self.health_cap_edit.setValue(self.savegame.health_cap)
        self.unlimited_flight_check.setChecked(not self.savegame.flying_needs_recharge)
        self.unlimited_breath_check.setChecked(not self.savegame.air_needed)
        self.money_edit.setValue(self.savegame.money)
        self.inventory_bars_edit.setValue(self.savegame.inventory_bars)

        self.wand_1_inventory_list.clear()
        self.wand_2_inventory_list.clear()
        self.wand_3_inventory_list.clear()
        self.wand_4_inventory_list.clear()
        self.inventory_list.clear()

        # ToDO: Put wands in their correct slots
        # ToDo: add cast delay
        try:
            wand_1: Wand = self.savegame.wands[0]
            self.wand_1_group_box.setTitle(wand_1.get_name())
            self.wand_1_mana_edit.setValue(wand_1.mana)
            self.wand_1_max_mana_edit.setValue(wand_1.mana_max)
            self.wand_1_mana_recharge_edit.setValue(wand_1.mana_recharge)
            self.wand_1_shuffle_check.setChecked(wand_1.shuffles)
            self.wand_1_spread_edit.setValue(wand_1.spread_degrees)
            self.wand_1_capacity_edit.setValue(wand_1.capacity)
            self.wand_1_spells_cast_edit.setValue(wand_1.spells_cast)
            self.wand_1_reload_time_edit.setValue(wand_1.reload_time)

            for spell in wand_1.cards:
                self.wand_1_inventory_list.addItem(spell.get_action_id())
        except IndexError:
            self.wand_1_group_box.setTitle("Empty Slot")

        try:
            wand_2: Wand = self.savegame.wands[1]
            self.wand_2_group_box.setTitle(wand_2.get_name())
            self.wand_2_mana_edit.setValue(wand_2.mana)
            self.wand_2_max_mana_edit.setValue(wand_2.mana_max)
            self.wand_2_mana_recharge_edit.setValue(wand_2.mana_recharge)
            self.wand_2_shuffle_check.setChecked(wand_2.shuffles)
            self.wand_2_spread_edit.setValue(wand_2.spread_degrees)
            self.wand_2_capacity_edit.setValue(wand_2.capacity)
            self.wand_2_spells_cast_edit.setValue(wand_2.spells_cast)
            self.wand_2_reload_time_edit.setValue(wand_2.reload_time)

            for spell in wand_2.cards:
                self.wand_2_inventory_list.addItem(spell.get_action_id())
        except IndexError:
            self.wand_2_group_box.setTitle("Empty Slot")

        try:
            wand_3: Wand = self.savegame.wands[2]
            self.wand_3_group_box.setTitle(wand_3.get_name())
            self.wand_3_mana_edit.setValue(wand_3.mana)
            self.wand_3_max_mana_edit.setValue(wand_3.mana_max)
            self.wand_3_mana_recharge_edit.setValue(wand_3.mana_recharge)
            self.wand_3_shuffle_check.setChecked(wand_3.shuffles)
            self.wand_3_spread_edit.setValue(wand_3.spread_degrees)
            self.wand_3_capacity_edit.setValue(wand_3.capacity)
            self.wand_3_spells_cast_edit.setValue(wand_3.spells_cast)
            self.wand_3_reload_time_edit.setValue(wand_3.reload_time)

            for spell in wand_3.cards:
                self.wand_3_inventory_list.addItem(spell.get_action_id())
        except IndexError:
            self.wand_3_group_box.setTitle("Empty Slot")

        try:
            wand_4: Wand = self.savegame.wands[3]
            self.wand_4_group_box.setTitle(wand_4.get_name())
            self.wand_4_mana_edit.setValue(wand_4.mana)
            self.wand_4_max_mana_edit.setValue(wand_4.mana_max)
            self.wand_4_mana_recharge_edit.setValue(wand_4.mana_recharge)
            self.wand_4_shuffle_check.setChecked(wand_4.shuffles)
            self.wand_4_spread_edit.setValue(wand_4.spread_degrees)
            self.wand_4_capacity_edit.setValue(wand_4.capacity)
            self.wand_4_spells_cast_edit.setValue(wand_4.spells_cast)
            self.wand_4_reload_time_edit.setValue(wand_4.reload_time)

            for spell in wand_4.cards:
                self.wand_4_inventory_list.addItem(spell.get_action_id())
        except IndexError:
            self.wand_4_group_box.setTitle("Empty Slot")

        for card in self.savegame.inventory:
            self.inventory_list.addItem(card.get_action_id())


if __name__ == '__main__':
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec_()
