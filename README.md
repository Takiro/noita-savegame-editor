# Noita Savegame-Editor

This is a small program that allows editing a Noita Savegame. I primarily made it to export my inventory to a file, when I had a good run, and then import it later to a new game, to have the spells and wands from the previous from the start.  

This was never intended as an extensive chat tool but I added some more options because I had fun programming it, and as a reference for others who maybe want to extend it. I made it for my personal use but maybe someone else will find this useful too.

# Features

Currently the editor can change the following option:

## Character stats

- Health
- Max Health
- Health Cap
- Unlimited Flight
- Unlimited Breath (you don't run out of air when submerged in liquids anymore)
- Money
- How many bars your inventory has (up to 16, the maximum that fits on the screen)


## Wands

For each wand you can edit

- Mana
- Max Mana
- Mana Recharge
- Shuffle
- Spread
- Reload Time
- Capacity
- Spells cast

## Export/Import

The editor has a Export function that allows you to export your current inventory (Wands, Spells, Items) to a XML file. This file can be imported into another savegame.
For the import option to be enabled you first have to load/open the savegame (the `player.xml`) you want to import to. Then click `File -> Import...` and choose the inventory file. The editor interface should update the values now and fill the fields with the imported items. Now chose `Save` and start the game. You should now have your items back. Keep in mind that the import feature **replaces the items** of the savegame it is imported to, not adding to it. This means you lose what you had before.

# Currently not supported

Currently the Spells of the Wands and in your inventory are read only and can't be edited. This feature may be implemented in the future as I initially planed to have it (some methods in the Savegame class are already there, like changing the remaining uses oft Spells with limited uses).

Adding arbitrary spells to the inventory or to wands will probably never be implemented because of the way they stored, it would be too much work.

Editing other items like potions is not implemented and was never planed to be implemented. However the export/import function do export/import them too, even though it's not sown in the UI.


# Installation and running
For Windows 10 and 11 (probably works on older windows too) there is an executable you can download from the [release page](https://github.com/Takiro/noita-savegame-editor/releases). It should run without any aditionall steps.

Alternatively you can install it manually with the following steps:  
- Have Python 3.8 or newer installed. If you are on Linux or some Macs, you probably already have it.
- install the dependencies with `pip install -r requirements.txt` from the command line while in the directory you downloaded the sources to. This installs qt5 (needed for the GUI) and defusedxml (a safe xml parser library)
- run `python main.py` with python from a terminal or by double clicking it (depends a bit on your operating system)

This application was tested on Windows and Linux but should also run on Mac if manually installed.

# Caution
Keep in mind that you should back up your savegames in case something goes wrong. These kind of tools can always break something unexpectedly.
