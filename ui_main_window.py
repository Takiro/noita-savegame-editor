# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(864, 835)
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        self.action_save = QAction(MainWindow)
        self.action_save.setObjectName(u"action_save")
        self.action_save.setEnabled(False)
        self.action_export_inventory = QAction(MainWindow)
        self.action_export_inventory.setObjectName(u"action_export_inventory")
        self.action_export_inventory.setEnabled(False)
        self.action_import_inventory = QAction(MainWindow)
        self.action_import_inventory.setObjectName(u"action_import_inventory")
        self.action_import_inventory.setEnabled(False)
        self.action_quit = QAction(MainWindow)
        self.action_quit.setObjectName(u"action_quit")
        self.action_quick_load = QAction(MainWindow)
        self.action_quick_load.setObjectName(u"action_quick_load")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 2, 1)

        self.unlimited_flight_check = QCheckBox(self.groupBox)
        self.unlimited_flight_check.setObjectName(u"unlimited_flight_check")

        self.gridLayout.addWidget(self.unlimited_flight_check, 0, 3, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.unlimited_breath_check = QCheckBox(self.groupBox)
        self.unlimited_breath_check.setObjectName(u"unlimited_breath_check")

        self.gridLayout.addWidget(self.unlimited_breath_check, 1, 3, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 3, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)

        self.health_edit = QSpinBox(self.groupBox)
        self.health_edit.setObjectName(u"health_edit")
        self.health_edit.setFrame(True)
        self.health_edit.setMaximum(999999999)
        self.health_edit.setSingleStep(10)

        self.gridLayout.addWidget(self.health_edit, 0, 1, 1, 1)

        self.max_health_edit = QSpinBox(self.groupBox)
        self.max_health_edit.setObjectName(u"max_health_edit")
        self.max_health_edit.setMaximum(999999999)
        self.max_health_edit.setSingleStep(10)

        self.gridLayout.addWidget(self.max_health_edit, 1, 1, 1, 1)

        self.health_cap_edit = QSpinBox(self.groupBox)
        self.health_cap_edit.setObjectName(u"health_cap_edit")
        self.health_cap_edit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.health_cap_edit.setMaximum(999999999)
        self.health_cap_edit.setSingleStep(10)

        self.gridLayout.addWidget(self.health_cap_edit, 3, 1, 1, 1)

        self.money_edit = QSpinBox(self.groupBox)
        self.money_edit.setObjectName(u"money_edit")
        self.money_edit.setMaximum(999999999)
        self.money_edit.setSingleStep(100)

        self.gridLayout.addWidget(self.money_edit, 3, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_7.addWidget(self.groupBox)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.wand_4_group_box = QGroupBox(self.centralwidget)
        self.wand_4_group_box.setObjectName(u"wand_4_group_box")
        self.verticalLayout_6 = QVBoxLayout(self.wand_4_group_box)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(10)
        self.label_31 = QLabel(self.wand_4_group_box)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_31, 3, 2, 1, 1)

        self.wand_4_reload_time_edit = QDoubleSpinBox(self.wand_4_group_box)
        self.wand_4_reload_time_edit.setObjectName(u"wand_4_reload_time_edit")
        self.wand_4_reload_time_edit.setMaximum(36000.000000000000000)

        self.gridLayout_5.addWidget(self.wand_4_reload_time_edit, 1, 3, 1, 1)

        self.label_32 = QLabel(self.wand_4_group_box)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_32, 0, 2, 1, 1)

        self.label_33 = QLabel(self.wand_4_group_box)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_33, 1, 2, 1, 1)

        self.label_34 = QLabel(self.wand_4_group_box)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_34, 0, 0, 1, 1)

        self.label_35 = QLabel(self.wand_4_group_box)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_35, 1, 0, 2, 1)

        self.label_36 = QLabel(self.wand_4_group_box)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_36, 3, 0, 1, 1)

        self.wand_4_spread_edit = QDoubleSpinBox(self.wand_4_group_box)
        self.wand_4_spread_edit.setObjectName(u"wand_4_spread_edit")
        self.wand_4_spread_edit.setMaximum(1800.000000000000000)

        self.gridLayout_5.addWidget(self.wand_4_spread_edit, 0, 3, 1, 1)

        self.label_37 = QLabel(self.wand_4_group_box)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_37, 4, 0, 1, 1)

        self.wand_4_shuffle_check = QCheckBox(self.wand_4_group_box)
        self.wand_4_shuffle_check.setObjectName(u"wand_4_shuffle_check")

        self.gridLayout_5.addWidget(self.wand_4_shuffle_check, 4, 1, 1, 1)

        self.label_38 = QLabel(self.wand_4_group_box)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_38, 4, 2, 1, 1)

        self.wand_4_spells_cast_edit = QSpinBox(self.wand_4_group_box)
        self.wand_4_spells_cast_edit.setObjectName(u"wand_4_spells_cast_edit")
        self.wand_4_spells_cast_edit.setMinimum(1)
        self.wand_4_spells_cast_edit.setMaximum(30)

        self.gridLayout_5.addWidget(self.wand_4_spells_cast_edit, 4, 3, 1, 1)

        self.wand_4_capacity_edit = QSpinBox(self.wand_4_group_box)
        self.wand_4_capacity_edit.setObjectName(u"wand_4_capacity_edit")
        self.wand_4_capacity_edit.setMinimum(1)
        self.wand_4_capacity_edit.setMaximum(30)

        self.gridLayout_5.addWidget(self.wand_4_capacity_edit, 3, 3, 1, 1)

        self.wand_4_mana_edit = QSpinBox(self.wand_4_group_box)
        self.wand_4_mana_edit.setObjectName(u"wand_4_mana_edit")
        self.wand_4_mana_edit.setMaximum(999999999)
        self.wand_4_mana_edit.setSingleStep(10)

        self.gridLayout_5.addWidget(self.wand_4_mana_edit, 0, 1, 1, 1)

        self.wand_4_max_mana_edit = QSpinBox(self.wand_4_group_box)
        self.wand_4_max_mana_edit.setObjectName(u"wand_4_max_mana_edit")
        self.wand_4_max_mana_edit.setMaximum(999999999)
        self.wand_4_max_mana_edit.setSingleStep(10)

        self.gridLayout_5.addWidget(self.wand_4_max_mana_edit, 1, 1, 1, 1)

        self.wand_4_mana_recharge_edit = QSpinBox(self.wand_4_group_box)
        self.wand_4_mana_recharge_edit.setObjectName(u"wand_4_mana_recharge_edit")
        self.wand_4_mana_recharge_edit.setMaximum(999999999)
        self.wand_4_mana_recharge_edit.setSingleStep(10)

        self.gridLayout_5.addWidget(self.wand_4_mana_recharge_edit, 3, 1, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_5)

        self.wand_4_inventory_list = QListWidget(self.wand_4_group_box)
        self.wand_4_inventory_list.setObjectName(u"wand_4_inventory_list")

        self.verticalLayout_6.addWidget(self.wand_4_inventory_list)


        self.gridLayout_6.addWidget(self.wand_4_group_box, 1, 1, 1, 1)

        self.wand_3_group_box = QGroupBox(self.centralwidget)
        self.wand_3_group_box.setObjectName(u"wand_3_group_box")
        self.verticalLayout_3 = QVBoxLayout(self.wand_3_group_box)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(10)
        self.label_15 = QLabel(self.wand_3_group_box)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_15, 3, 2, 1, 1)

        self.wand_3_reload_time_edit = QDoubleSpinBox(self.wand_3_group_box)
        self.wand_3_reload_time_edit.setObjectName(u"wand_3_reload_time_edit")
        self.wand_3_reload_time_edit.setMaximum(36000.000000000000000)

        self.gridLayout_3.addWidget(self.wand_3_reload_time_edit, 1, 3, 1, 1)

        self.label_16 = QLabel(self.wand_3_group_box)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_16, 0, 2, 1, 1)

        self.label_17 = QLabel(self.wand_3_group_box)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_17, 1, 2, 1, 1)

        self.label_18 = QLabel(self.wand_3_group_box)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_18, 0, 0, 1, 1)

        self.label_19 = QLabel(self.wand_3_group_box)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_19, 1, 0, 2, 1)

        self.label_20 = QLabel(self.wand_3_group_box)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_20, 3, 0, 1, 1)

        self.wand_3_spread_edit = QDoubleSpinBox(self.wand_3_group_box)
        self.wand_3_spread_edit.setObjectName(u"wand_3_spread_edit")
        self.wand_3_spread_edit.setMaximum(1800.000000000000000)

        self.gridLayout_3.addWidget(self.wand_3_spread_edit, 0, 3, 1, 1)

        self.label_21 = QLabel(self.wand_3_group_box)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_21, 4, 0, 1, 1)

        self.wand_3_shuffle_check = QCheckBox(self.wand_3_group_box)
        self.wand_3_shuffle_check.setObjectName(u"wand_3_shuffle_check")

        self.gridLayout_3.addWidget(self.wand_3_shuffle_check, 4, 1, 1, 1)

        self.label_22 = QLabel(self.wand_3_group_box)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_22, 4, 2, 1, 1)

        self.wand_3_spells_cast_edit = QSpinBox(self.wand_3_group_box)
        self.wand_3_spells_cast_edit.setObjectName(u"wand_3_spells_cast_edit")
        self.wand_3_spells_cast_edit.setMinimum(1)
        self.wand_3_spells_cast_edit.setMaximum(30)

        self.gridLayout_3.addWidget(self.wand_3_spells_cast_edit, 4, 3, 1, 1)

        self.wand_3_capacity_edit = QSpinBox(self.wand_3_group_box)
        self.wand_3_capacity_edit.setObjectName(u"wand_3_capacity_edit")
        self.wand_3_capacity_edit.setMinimum(1)
        self.wand_3_capacity_edit.setMaximum(30)

        self.gridLayout_3.addWidget(self.wand_3_capacity_edit, 3, 3, 1, 1)

        self.wand_3_mana_edit = QSpinBox(self.wand_3_group_box)
        self.wand_3_mana_edit.setObjectName(u"wand_3_mana_edit")
        self.wand_3_mana_edit.setMaximum(999999999)
        self.wand_3_mana_edit.setSingleStep(10)

        self.gridLayout_3.addWidget(self.wand_3_mana_edit, 0, 1, 1, 1)

        self.wand_3_max_mana_edit = QSpinBox(self.wand_3_group_box)
        self.wand_3_max_mana_edit.setObjectName(u"wand_3_max_mana_edit")
        self.wand_3_max_mana_edit.setMaximum(999999999)
        self.wand_3_max_mana_edit.setSingleStep(10)

        self.gridLayout_3.addWidget(self.wand_3_max_mana_edit, 1, 1, 1, 1)

        self.wand_3_mana_recharge_edit = QSpinBox(self.wand_3_group_box)
        self.wand_3_mana_recharge_edit.setObjectName(u"wand_3_mana_recharge_edit")
        self.wand_3_mana_recharge_edit.setMaximum(999999999)
        self.wand_3_mana_recharge_edit.setSingleStep(10)

        self.gridLayout_3.addWidget(self.wand_3_mana_recharge_edit, 3, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)

        self.wand_3_inventory_list = QListWidget(self.wand_3_group_box)
        self.wand_3_inventory_list.setObjectName(u"wand_3_inventory_list")

        self.verticalLayout_3.addWidget(self.wand_3_inventory_list)


        self.gridLayout_6.addWidget(self.wand_3_group_box, 1, 0, 1, 1)

        self.wand_1_group_box = QGroupBox(self.centralwidget)
        self.wand_1_group_box.setObjectName(u"wand_1_group_box")
        self.verticalLayout_5 = QVBoxLayout(self.wand_1_group_box)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(10)
        self.gridLayout_4.setVerticalSpacing(6)
        self.label_23 = QLabel(self.wand_1_group_box)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_23, 3, 2, 1, 1)

        self.wand_1_reload_time_edit = QDoubleSpinBox(self.wand_1_group_box)
        self.wand_1_reload_time_edit.setObjectName(u"wand_1_reload_time_edit")
        self.wand_1_reload_time_edit.setMaximum(36000.000000000000000)

        self.gridLayout_4.addWidget(self.wand_1_reload_time_edit, 1, 3, 1, 1)

        self.label_24 = QLabel(self.wand_1_group_box)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_24, 0, 2, 1, 1)

        self.label_25 = QLabel(self.wand_1_group_box)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_25, 1, 2, 1, 1)

        self.label_26 = QLabel(self.wand_1_group_box)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_26, 0, 0, 1, 1)

        self.label_27 = QLabel(self.wand_1_group_box)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_27, 1, 0, 2, 1)

        self.label_28 = QLabel(self.wand_1_group_box)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_28, 3, 0, 1, 1)

        self.wand_1_spread_edit = QDoubleSpinBox(self.wand_1_group_box)
        self.wand_1_spread_edit.setObjectName(u"wand_1_spread_edit")
        self.wand_1_spread_edit.setMaximum(1800.000000000000000)

        self.gridLayout_4.addWidget(self.wand_1_spread_edit, 0, 3, 1, 1)

        self.label_29 = QLabel(self.wand_1_group_box)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_29, 4, 0, 1, 1)

        self.wand_1_shuffle_check = QCheckBox(self.wand_1_group_box)
        self.wand_1_shuffle_check.setObjectName(u"wand_1_shuffle_check")

        self.gridLayout_4.addWidget(self.wand_1_shuffle_check, 4, 1, 1, 1)

        self.label_30 = QLabel(self.wand_1_group_box)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_30, 4, 2, 1, 1)

        self.wand_1_spells_cast_edit = QSpinBox(self.wand_1_group_box)
        self.wand_1_spells_cast_edit.setObjectName(u"wand_1_spells_cast_edit")
        self.wand_1_spells_cast_edit.setMinimum(1)
        self.wand_1_spells_cast_edit.setMaximum(30)

        self.gridLayout_4.addWidget(self.wand_1_spells_cast_edit, 4, 3, 1, 1)

        self.wand_1_capacity_edit = QSpinBox(self.wand_1_group_box)
        self.wand_1_capacity_edit.setObjectName(u"wand_1_capacity_edit")
        self.wand_1_capacity_edit.setMinimum(1)
        self.wand_1_capacity_edit.setMaximum(30)

        self.gridLayout_4.addWidget(self.wand_1_capacity_edit, 3, 3, 1, 1)

        self.wand_1_mana_edit = QSpinBox(self.wand_1_group_box)
        self.wand_1_mana_edit.setObjectName(u"wand_1_mana_edit")
        self.wand_1_mana_edit.setMaximum(999999999)
        self.wand_1_mana_edit.setSingleStep(10)

        self.gridLayout_4.addWidget(self.wand_1_mana_edit, 0, 1, 1, 1)

        self.wand_1_max_mana_edit = QSpinBox(self.wand_1_group_box)
        self.wand_1_max_mana_edit.setObjectName(u"wand_1_max_mana_edit")
        self.wand_1_max_mana_edit.setMaximum(999999999)
        self.wand_1_max_mana_edit.setSingleStep(10)

        self.gridLayout_4.addWidget(self.wand_1_max_mana_edit, 1, 1, 1, 1)

        self.wand_1_mana_recharge_edit = QSpinBox(self.wand_1_group_box)
        self.wand_1_mana_recharge_edit.setObjectName(u"wand_1_mana_recharge_edit")
        self.wand_1_mana_recharge_edit.setMaximum(999999999)
        self.wand_1_mana_recharge_edit.setSingleStep(10)

        self.gridLayout_4.addWidget(self.wand_1_mana_recharge_edit, 3, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_4)

        self.wand_1_inventory_list = QListWidget(self.wand_1_group_box)
        self.wand_1_inventory_list.setObjectName(u"wand_1_inventory_list")

        self.verticalLayout_5.addWidget(self.wand_1_inventory_list)


        self.gridLayout_6.addWidget(self.wand_1_group_box, 0, 0, 1, 1)

        self.wand_2_group_box = QGroupBox(self.centralwidget)
        self.wand_2_group_box.setObjectName(u"wand_2_group_box")
        self.verticalLayout_2 = QVBoxLayout(self.wand_2_group_box)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.label_12 = QLabel(self.wand_2_group_box)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_12, 3, 2, 1, 1)

        self.wand_2_reload_time_edit = QDoubleSpinBox(self.wand_2_group_box)
        self.wand_2_reload_time_edit.setObjectName(u"wand_2_reload_time_edit")
        self.wand_2_reload_time_edit.setMaximum(36000.000000000000000)

        self.gridLayout_2.addWidget(self.wand_2_reload_time_edit, 1, 3, 1, 1)

        self.label_8 = QLabel(self.wand_2_group_box)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_8, 0, 2, 1, 1)

        self.label_10 = QLabel(self.wand_2_group_box)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_10, 1, 2, 1, 1)

        self.label_7 = QLabel(self.wand_2_group_box)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_9 = QLabel(self.wand_2_group_box)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 2, 1)

        self.label_11 = QLabel(self.wand_2_group_box)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)

        self.wand_2_spread_edit = QDoubleSpinBox(self.wand_2_group_box)
        self.wand_2_spread_edit.setObjectName(u"wand_2_spread_edit")
        self.wand_2_spread_edit.setMaximum(1800.000000000000000)

        self.gridLayout_2.addWidget(self.wand_2_spread_edit, 0, 3, 1, 1)

        self.label_13 = QLabel(self.wand_2_group_box)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_13, 4, 0, 1, 1)

        self.wand_2_shuffle_check = QCheckBox(self.wand_2_group_box)
        self.wand_2_shuffle_check.setObjectName(u"wand_2_shuffle_check")

        self.gridLayout_2.addWidget(self.wand_2_shuffle_check, 4, 1, 1, 1)

        self.label_14 = QLabel(self.wand_2_group_box)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_14, 4, 2, 1, 1)

        self.wand_2_spells_cast_edit = QSpinBox(self.wand_2_group_box)
        self.wand_2_spells_cast_edit.setObjectName(u"wand_2_spells_cast_edit")
        self.wand_2_spells_cast_edit.setMinimum(1)
        self.wand_2_spells_cast_edit.setMaximum(30)

        self.gridLayout_2.addWidget(self.wand_2_spells_cast_edit, 4, 3, 1, 1)

        self.wand_2_capacity_edit = QSpinBox(self.wand_2_group_box)
        self.wand_2_capacity_edit.setObjectName(u"wand_2_capacity_edit")
        self.wand_2_capacity_edit.setMinimum(1)
        self.wand_2_capacity_edit.setMaximum(30)

        self.gridLayout_2.addWidget(self.wand_2_capacity_edit, 3, 3, 1, 1)

        self.wand_2_mana_edit = QSpinBox(self.wand_2_group_box)
        self.wand_2_mana_edit.setObjectName(u"wand_2_mana_edit")
        self.wand_2_mana_edit.setMaximum(999999999)
        self.wand_2_mana_edit.setSingleStep(10)

        self.gridLayout_2.addWidget(self.wand_2_mana_edit, 0, 1, 1, 1)

        self.wand_2_max_mana_edit = QSpinBox(self.wand_2_group_box)
        self.wand_2_max_mana_edit.setObjectName(u"wand_2_max_mana_edit")
        self.wand_2_max_mana_edit.setMaximum(999999999)
        self.wand_2_max_mana_edit.setSingleStep(10)

        self.gridLayout_2.addWidget(self.wand_2_max_mana_edit, 1, 1, 1, 1)

        self.wand_2_mana_recharge_edit = QSpinBox(self.wand_2_group_box)
        self.wand_2_mana_recharge_edit.setObjectName(u"wand_2_mana_recharge_edit")
        self.wand_2_mana_recharge_edit.setMaximum(999999999)
        self.wand_2_mana_recharge_edit.setSingleStep(10)

        self.gridLayout_2.addWidget(self.wand_2_mana_recharge_edit, 3, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.wand_2_inventory_list = QListWidget(self.wand_2_group_box)
        self.wand_2_inventory_list.setObjectName(u"wand_2_inventory_list")

        self.verticalLayout_2.addWidget(self.wand_2_inventory_list)


        self.gridLayout_6.addWidget(self.wand_2_group_box, 0, 1, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_6)


        self.horizontalLayout.addLayout(self.verticalLayout_7)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_39 = QLabel(self.groupBox_2)
        self.label_39.setObjectName(u"label_39")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_39)

        self.inventory_bars_edit = QSpinBox(self.groupBox_2)
        self.inventory_bars_edit.setObjectName(u"inventory_bars_edit")
        self.inventory_bars_edit.setMinimum(1)
        self.inventory_bars_edit.setMaximum(16)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.inventory_bars_edit)

        self.label_40 = QLabel(self.groupBox_2)
        self.label_40.setObjectName(u"label_40")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_40)

        self.inventory_use_label = QLabel(self.groupBox_2)
        self.inventory_use_label.setObjectName(u"inventory_use_label")
        self.inventory_use_label.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.inventory_use_label)


        self.verticalLayout_4.addLayout(self.formLayout)

        self.inventory_list = QListWidget(self.groupBox_2)
        self.inventory_list.setObjectName(u"inventory_list")

        self.verticalLayout_4.addWidget(self.inventory_list)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)


        self.horizontalLayout.addWidget(self.groupBox_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 864, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.action_quick_load)
        self.menuFile.addAction(self.action_open)
        self.menuFile.addAction(self.action_save)
        self.menuFile.addAction(self.action_export_inventory)
        self.menuFile.addAction(self.action_import_inventory)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_quit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Noita Save-Editor", None))
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"Open...", None))
#if QT_CONFIG(tooltip)
        self.action_open.setToolTip(QCoreApplication.translate("MainWindow", u"Choose a Noita savegame to load", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_open.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(tooltip)
        self.action_save.setToolTip(QCoreApplication.translate("MainWindow", u"Save current file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_save.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_export_inventory.setText(QCoreApplication.translate("MainWindow", u"Export...", None))
#if QT_CONFIG(tooltip)
        self.action_export_inventory.setToolTip(QCoreApplication.translate("MainWindow", u"Export current inventory and wands to file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_export_inventory.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.action_import_inventory.setText(QCoreApplication.translate("MainWindow", u"Import...", None))
#if QT_CONFIG(tooltip)
        self.action_import_inventory.setToolTip(QCoreApplication.translate("MainWindow", u"Import a currently exported and inventory with wands", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_import_inventory.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.action_quit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.action_quit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.action_quick_load.setText(QCoreApplication.translate("MainWindow", u"Load", None))
#if QT_CONFIG(tooltip)
        self.action_quick_load.setToolTip(QCoreApplication.translate("MainWindow", u"Automatically looks for the save fille of the current and opens it, if possible.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_quick_load.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Character", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Max Health", None))
        self.unlimited_flight_check.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Health Cap", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Unlimited Flight", None))
        self.unlimited_breath_check.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Health", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Money", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Unlimited Breath", None))
        self.wand_4_group_box.setTitle(QCoreApplication.translate("MainWindow", u"Wand 4", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Capacity", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Spread", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Relaod Time", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Mana", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Max Mana", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Mana Recharge", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Shuffle", None))
        self.wand_4_shuffle_check.setText(QCoreApplication.translate("MainWindow", u"no", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Spells Cast", None))
        self.wand_3_group_box.setTitle(QCoreApplication.translate("MainWindow", u"Wand 3", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Capacity", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Spread", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Relaod Time", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Mana", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Max Mana", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Mana Recharge", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Shuffle", None))
        self.wand_3_shuffle_check.setText(QCoreApplication.translate("MainWindow", u"no", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Spells Cast", None))
        self.wand_1_group_box.setTitle(QCoreApplication.translate("MainWindow", u"Wand 1", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Capacity", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Spread", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Relaod Time", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Mana", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Max Mana", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Mana Recharge", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Shuffle", None))
        self.wand_1_shuffle_check.setText(QCoreApplication.translate("MainWindow", u"no", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Spells Cast", None))
        self.wand_2_group_box.setTitle(QCoreApplication.translate("MainWindow", u"Wand 2", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Capacity", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Spread", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Relaod Time", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Mana", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Max Mana", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Mana Recharge", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Shuffle", None))
        self.wand_2_shuffle_check.setText(QCoreApplication.translate("MainWindow", u"no", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Spells Cast", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Inventory", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Inventory Bars", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Nummer of slots:", None))
        self.inventory_use_label.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

