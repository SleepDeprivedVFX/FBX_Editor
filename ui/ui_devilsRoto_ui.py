# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'devilsRoto_uirfFKAu.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_DevilsRotoscope(object):
    def setupUi(self, DevilsRotoscope):
        if DevilsRotoscope.objectName():
            DevilsRotoscope.setObjectName(u"DevilsRotoscope")
        DevilsRotoscope.resize(741, 558)
        DevilsRotoscope.setStyleSheet(u"background-color: rgb(100, 100, 100);\n"
"color: rgb(230, 230, 230);")
        self.verticalLayout_4 = QVBoxLayout(DevilsRotoscope)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Title = QLabel(DevilsRotoscope)
        self.Title.setObjectName(u"Title")
        self.Title.setStyleSheet(u"font: 22pt \"Tempus Sans ITC\";\n"
"color: rgb(220, 220, 220);")

        self.verticalLayout_4.addWidget(self.Title)

        self.toolboxes = QTabWidget(DevilsRotoscope)
        self.toolboxes.setObjectName(u"toolboxes")
        self.toolboxes.setStyleSheet(u"QTabBar::tab {\n"
"     border: 2px solid #C4C4C3;\n"
"     border-bottom-color: #C2C7CB;\n"
"     border-top-left-radius: 6px;\n"
"     border-top-right-radius: 6px;\n"
"     min-width: 8ex;\n"
"     padding: 2px;\n"
" }\n"
"QTabWidget {\n"
"	border: 2px;\n"
"}")
        self.toolboxes.setDocumentMode(False)
        self.toolboxes.setTabBarAutoHide(False)
        self.Playblaster = QWidget()
        self.Playblaster.setObjectName(u"Playblaster")
        self.verticalLayout_2 = QVBoxLayout(self.Playblaster)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.process_grp = QGroupBox(self.Playblaster)
        self.process_grp.setObjectName(u"process_grp")
        self.process_grp.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_4 = QHBoxLayout(self.process_grp)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_batch_btn = QRadioButton(self.process_grp)
        self.pb_batch_btn.setObjectName(u"pb_batch_btn")
        self.pb_batch_btn.setChecked(True)

        self.horizontalLayout.addWidget(self.pb_batch_btn)

        self.pb_file_btn = QRadioButton(self.process_grp)
        self.pb_file_btn.setObjectName(u"pb_file_btn")

        self.horizontalLayout.addWidget(self.pb_file_btn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.process_grp)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pb_folder_file_label = QLabel(self.Playblaster)
        self.pb_folder_file_label.setObjectName(u"pb_folder_file_label")

        self.horizontalLayout_2.addWidget(self.pb_folder_file_label)

        self.pb_folder_file = QLineEdit(self.Playblaster)
        self.pb_folder_file.setObjectName(u"pb_folder_file")

        self.horizontalLayout_2.addWidget(self.pb_folder_file)

        self.pb_browse_btn = QPushButton(self.Playblaster)
        self.pb_browse_btn.setObjectName(u"pb_browse_btn")

        self.horizontalLayout_2.addWidget(self.pb_browse_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pb_origin_label = QLabel(self.Playblaster)
        self.pb_origin_label.setObjectName(u"pb_origin_label")
        self.pb_origin_label.setToolTipDuration(-1)

        self.horizontalLayout_5.addWidget(self.pb_origin_label)

        self.pb_origin_angle = QDoubleSpinBox(self.Playblaster)
        self.pb_origin_angle.setObjectName(u"pb_origin_angle")

        self.horizontalLayout_5.addWidget(self.pb_origin_angle)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)

        self.pb_queue_btn = QPushButton(self.Playblaster)
        self.pb_queue_btn.setObjectName(u"pb_queue_btn")

        self.horizontalLayout_10.addWidget(self.pb_queue_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pb_queue_label = QLabel(self.Playblaster)
        self.pb_queue_label.setObjectName(u"pb_queue_label")

        self.verticalLayout.addWidget(self.pb_queue_label)

        self.pb_queue = QTableWidget(self.Playblaster)
        if (self.pb_queue.columnCount() < 3):
            self.pb_queue.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.pb_queue.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.pb_queue.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.pb_queue.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.pb_queue.setObjectName(u"pb_queue")
        self.pb_queue.setStyleSheet(u"QHeaderView::section{\n"
"	\n"
"	background-color: rgb(97, 97, 97);\n"
"}\n"
"QTableView::item{\n"
"	border: 0px;\n"
"	padding: 5px;\n"
"}")
        self.pb_queue.setAlternatingRowColors(True)
        self.pb_queue.horizontalHeader().setStretchLastSection(True)
        self.pb_queue.verticalHeader().setVisible(False)
        self.pb_queue.verticalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.pb_queue)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pb_cancel_btn = QPushButton(self.Playblaster)
        self.pb_cancel_btn.setObjectName(u"pb_cancel_btn")

        self.horizontalLayout_3.addWidget(self.pb_cancel_btn)

        self.pb_run_btn = QPushButton(self.Playblaster)
        self.pb_run_btn.setObjectName(u"pb_run_btn")

        self.horizontalLayout_3.addWidget(self.pb_run_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.toolboxes.addTab(self.Playblaster, "")
        self.exporter = QWidget()
        self.exporter.setObjectName(u"exporter")
        self.verticalLayout_3 = QVBoxLayout(self.exporter)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.process_grp_2 = QGroupBox(self.exporter)
        self.process_grp_2.setObjectName(u"process_grp_2")
        self.process_grp_2.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_7 = QHBoxLayout(self.process_grp_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.ex_batch_btn = QRadioButton(self.process_grp_2)
        self.ex_batch_btn.setObjectName(u"ex_batch_btn")
        self.ex_batch_btn.setChecked(True)

        self.horizontalLayout_8.addWidget(self.ex_batch_btn)

        self.ex_file_btn = QRadioButton(self.process_grp_2)
        self.ex_file_btn.setObjectName(u"ex_file_btn")

        self.horizontalLayout_8.addWidget(self.ex_file_btn)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)


        self.verticalLayout_3.addWidget(self.process_grp_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.ex_folder_file_label = QLabel(self.exporter)
        self.ex_folder_file_label.setObjectName(u"ex_folder_file_label")

        self.horizontalLayout_6.addWidget(self.ex_folder_file_label)

        self.ex_folder_file = QLineEdit(self.exporter)
        self.ex_folder_file.setObjectName(u"ex_folder_file")

        self.horizontalLayout_6.addWidget(self.ex_folder_file)

        self.ex_browse_btn = QPushButton(self.exporter)
        self.ex_browse_btn.setObjectName(u"ex_browse_btn")

        self.horizontalLayout_6.addWidget(self.ex_browse_btn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)

        self.ex_queue_btn = QPushButton(self.exporter)
        self.ex_queue_btn.setObjectName(u"ex_queue_btn")

        self.horizontalLayout_11.addWidget(self.ex_queue_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.ex_export_table = QTableWidget(self.exporter)
        if (self.ex_export_table.columnCount() < 7):
            self.ex_export_table.setColumnCount(7)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.ex_export_table.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.ex_export_table.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.ex_export_table.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.ex_export_table.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.ex_export_table.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.ex_export_table.setHorizontalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.ex_export_table.setHorizontalHeaderItem(6, __qtablewidgetitem9)
        if (self.ex_export_table.rowCount() < 1):
            self.ex_export_table.setRowCount(1)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.ex_export_table.setVerticalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.ex_export_table.setItem(0, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.ex_export_table.setItem(0, 1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.ex_export_table.setItem(0, 2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.ex_export_table.setItem(0, 3, __qtablewidgetitem14)
        self.ex_export_table.setObjectName(u"ex_export_table")
        self.ex_export_table.setStyleSheet(u"QHeaderView::section{\n"
"	\n"
"	background-color: rgb(97, 97, 97);\n"
"}\n"
"QTableView::item{\n"
"	border: 0px;\n"
"	padding: 5px;\n"
"}")
        self.ex_export_table.setAlternatingRowColors(True)
        self.ex_export_table.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.ex_export_table)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.ex_cancel_btn = QPushButton(self.exporter)
        self.ex_cancel_btn.setObjectName(u"ex_cancel_btn")

        self.horizontalLayout_9.addWidget(self.ex_cancel_btn)

        self.ex_run_btn = QPushButton(self.exporter)
        self.ex_run_btn.setObjectName(u"ex_run_btn")

        self.horizontalLayout_9.addWidget(self.ex_run_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.toolboxes.addTab(self.exporter, "")
        self.config = QWidget()
        self.config.setObjectName(u"config")
        self.verticalLayout_8 = QVBoxLayout(self.config)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.cfg_maya = QGroupBox(self.config)
        self.cfg_maya.setObjectName(u"cfg_maya")
        self.verticalLayout_5 = QVBoxLayout(self.cfg_maya)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.cfg_maya_batch_path_label = QLabel(self.cfg_maya)
        self.cfg_maya_batch_path_label.setObjectName(u"cfg_maya_batch_path_label")

        self.horizontalLayout_12.addWidget(self.cfg_maya_batch_path_label)

        self.cfg_maya_batch_path = QLineEdit(self.cfg_maya)
        self.cfg_maya_batch_path.setObjectName(u"cfg_maya_batch_path")

        self.horizontalLayout_12.addWidget(self.cfg_maya_batch_path)

        self.cfg_mayabatch_btn = QPushButton(self.cfg_maya)
        self.cfg_mayabatch_btn.setObjectName(u"cfg_mayabatch_btn")

        self.horizontalLayout_12.addWidget(self.cfg_mayabatch_btn)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.cfg_mayapy_path_label = QLabel(self.cfg_maya)
        self.cfg_mayapy_path_label.setObjectName(u"cfg_mayapy_path_label")

        self.horizontalLayout_13.addWidget(self.cfg_mayapy_path_label)

        self.cfg_mayapy_path = QLineEdit(self.cfg_maya)
        self.cfg_mayapy_path.setObjectName(u"cfg_mayapy_path")

        self.horizontalLayout_13.addWidget(self.cfg_mayapy_path)

        self.cfg_mayapy_btn = QPushButton(self.cfg_maya)
        self.cfg_mayapy_btn.setObjectName(u"cfg_mayapy_btn")

        self.horizontalLayout_13.addWidget(self.cfg_mayapy_btn)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)


        self.verticalLayout_8.addWidget(self.cfg_maya)

        self.cfg_logger = QGroupBox(self.config)
        self.cfg_logger.setObjectName(u"cfg_logger")
        self.verticalLayout_6 = QVBoxLayout(self.cfg_logger)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.cfg_debug_logging = QCheckBox(self.cfg_logger)
        self.cfg_debug_logging.setObjectName(u"cfg_debug_logging")
        self.cfg_debug_logging.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_17.addWidget(self.cfg_debug_logging)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_13)


        self.verticalLayout_6.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.cfg_num_days_logging_label = QLabel(self.cfg_logger)
        self.cfg_num_days_logging_label.setObjectName(u"cfg_num_days_logging_label")

        self.horizontalLayout_14.addWidget(self.cfg_num_days_logging_label)

        self.cfg_num_days_logging = QSpinBox(self.cfg_logger)
        self.cfg_num_days_logging.setObjectName(u"cfg_num_days_logging")

        self.horizontalLayout_14.addWidget(self.cfg_num_days_logging)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_12)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)


        self.verticalLayout_8.addWidget(self.cfg_logger)

        self.cfg_mocap = QGroupBox(self.config)
        self.cfg_mocap.setObjectName(u"cfg_mocap")
        self.verticalLayout_7 = QVBoxLayout(self.cfg_mocap)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.cfg_default_root_label = QLabel(self.cfg_mocap)
        self.cfg_default_root_label.setObjectName(u"cfg_default_root_label")

        self.horizontalLayout_15.addWidget(self.cfg_default_root_label)

        self.cfg_default_root = QLineEdit(self.cfg_mocap)
        self.cfg_default_root.setObjectName(u"cfg_default_root")

        self.horizontalLayout_15.addWidget(self.cfg_default_root)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_11)


        self.verticalLayout_7.addLayout(self.horizontalLayout_15)


        self.verticalLayout_8.addWidget(self.cfg_mocap)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_10)

        self.cfg_cancel_btn = QPushButton(self.config)
        self.cfg_cancel_btn.setObjectName(u"cfg_cancel_btn")

        self.horizontalLayout_16.addWidget(self.cfg_cancel_btn)

        self.cfg_run_btn = QPushButton(self.config)
        self.cfg_run_btn.setObjectName(u"cfg_run_btn")

        self.horizontalLayout_16.addWidget(self.cfg_run_btn)


        self.verticalLayout_8.addLayout(self.horizontalLayout_16)

        self.toolboxes.addTab(self.config, "")

        self.verticalLayout_4.addWidget(self.toolboxes)

#if QT_CONFIG(shortcut)
        self.pb_folder_file_label.setBuddy(self.pb_browse_btn)
        self.pb_queue_label.setBuddy(self.pb_queue_btn)
        self.ex_folder_file_label.setBuddy(self.ex_browse_btn)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(DevilsRotoscope)

        self.toolboxes.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(DevilsRotoscope)
    # setupUi

    def retranslateUi(self, DevilsRotoscope):
        DevilsRotoscope.setWindowTitle(QCoreApplication.translate("DevilsRotoscope", u"Devil's Rotoscope", None))
        self.Title.setText(QCoreApplication.translate("DevilsRotoscope", u"Devil's Rotoscope Mocap Tools", None))
#if QT_CONFIG(tooltip)
        self.process_grp.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#080808;\">Process Type</span></p><p><span style=\" font-weight:600; color:#080808;\">Batch</span><span style=\" color:#080808;\"> mode sets the tool to search through a folder structure and return all viable files.</span></p><p><span style=\" font-weight:600; color:#080808;\">File</span><span style=\" color:#080808;\"> mode sets the tool to process a specific file individually.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.process_grp.setTitle(QCoreApplication.translate("DevilsRotoscope", u"Process Type", None))
#if QT_CONFIG(tooltip)
        self.pb_batch_btn.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#080808;\">Batch Processing</span></p><p><span style=\" color:#080808;\">This mode runs the tool on an entire folder structure chosen below.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pb_batch_btn.setText(QCoreApplication.translate("DevilsRotoscope", u"Batch", None))
#if QT_CONFIG(tooltip)
        self.pb_file_btn.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#080808;\">File Processing</span></p><p>This mode processes a single file.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pb_file_btn.setText(QCoreApplication.translate("DevilsRotoscope", u"File", None))
#if QT_CONFIG(tooltip)
        self.pb_folder_file_label.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#0c0c0c;\">Folder / File</span></p><p><br/></p><p><span style=\" color:#0c0c0c;\">When the </span><span style=\" font-weight:600; color:#0c0c0c;\">Process Type</span><span style=\" color:#0c0c0c;\"> is set to </span><span style=\" font-weight:600; color:#0c0c0c;\">Batch</span><span style=\" color:#0c0c0c;\">, this field takes a folder as input.  When </span><span style=\" font-weight:600; color:#0c0c0c;\">Process Type</span><span style=\" color:#0c0c0c;\"> is set to </span><span style=\" font-weight:600; color:#0c0c0c;\">File</span><span style=\" color:#0c0c0c;\">, then the field requires an existing file as its input.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pb_folder_file_label.setText(QCoreApplication.translate("DevilsRotoscope", u"Folder / File", None))
#if QT_CONFIG(tooltip)
        self.pb_folder_file.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#0c0c0c;\">Folder / File</span></p><p><br/></p><p><span style=\" color:#0c0c0c;\">When the </span><span style=\" font-weight:600; color:#0c0c0c;\">Process Type</span><span style=\" color:#0c0c0c;\"> is set to </span><span style=\" font-weight:600; color:#0c0c0c;\">Batch</span><span style=\" color:#0c0c0c;\">, this field takes a folder as input.  When </span><span style=\" font-weight:600; color:#0c0c0c;\">Process Type</span><span style=\" color:#0c0c0c;\"> is set to </span><span style=\" font-weight:600; color:#0c0c0c;\">File</span><span style=\" color:#0c0c0c;\">, then the field requires an existing file as its input.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pb_browse_btn.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#0c0c0c;\">Folder / File</span></p><p><br/></p><p><span style=\" color:#0c0c0c;\">When the </span><span style=\" font-weight:600; color:#0c0c0c;\">Process Type</span><span style=\" color:#0c0c0c;\"> is set to </span><span style=\" font-weight:600; color:#0c0c0c;\">Batch</span><span style=\" color:#0c0c0c;\">, this field takes a folder as input.  When </span><span style=\" font-weight:600; color:#0c0c0c;\">Process Type</span><span style=\" color:#0c0c0c;\"> is set to </span><span style=\" font-weight:600; color:#0c0c0c;\">File</span><span style=\" color:#0c0c0c;\">, then the field requires an existing file as its input.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pb_browse_btn.setText(QCoreApplication.translate("DevilsRotoscope", u"Browse...", None))
#if QT_CONFIG(tooltip)
        self.pb_origin_label.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#080808;\">Stage Origin Angle</span></p><p><span style=\" color:#090909;\">This will be the compass bearing measured on set. Use a compass during capture sessions to get the bearing for the Z Axis. If none is found or entered, zero is assumed.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pb_origin_label.setText(QCoreApplication.translate("DevilsRotoscope", u"Stage Origin Angle (in degrees)", None))
#if QT_CONFIG(tooltip)
        self.pb_origin_angle.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#080808;\">Stage Origin Angle</span></p><p><span style=\" color:#080808;\">This will be the compass bearing measured on set. Use a compass during capture sessions to get the bearing for the Z Axis. If none is found or entered, zero is assumed.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pb_queue_btn.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#060606;\">Load Queue</span></p><p><span style=\" color:#060606;\">This button will force an update of the selected folder or file into the Queue below</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pb_queue_btn.setText(QCoreApplication.translate("DevilsRotoscope", u"Load Queue", None))
        self.pb_queue_label.setText(QCoreApplication.translate("DevilsRotoscope", u"Playblast Queue", None))
        ___qtablewidgetitem = self.pb_queue.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DevilsRotoscope", u"Filename", None));
        ___qtablewidgetitem1 = self.pb_queue.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DevilsRotoscope", u"Thumbnail", None));
        ___qtablewidgetitem2 = self.pb_queue.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DevilsRotoscope", u"Progress", None));
        self.pb_cancel_btn.setText(QCoreApplication.translate("DevilsRotoscope", u"Cancel", None))
        self.pb_run_btn.setText(QCoreApplication.translate("DevilsRotoscope", u"Run Playblasts", None))
        self.toolboxes.setTabText(self.toolboxes.indexOf(self.Playblaster), QCoreApplication.translate("DevilsRotoscope", u"Playblaster", None))
#if QT_CONFIG(tooltip)
        self.toolboxes.setTabToolTip(self.toolboxes.indexOf(self.Playblaster), QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#040404;\">Playblaster</span></p><p><span style=\" color:#040404;\">The Playblaster puts out movie files of the FBX raw data that comes in from the MoCap Session.  It can be used in batch mode, or on a single FBX file.  If the stage orientation is known, this can be put into the system to adjust the forward direction of the Z Axis.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.process_grp_2.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#080808;\">Process Type</span></p><p><span style=\" font-weight:600; color:#080808;\">Batch</span><span style=\" color:#080808;\"> mode sets the tool to search through a folder structure and return all viable files.</span></p><p><span style=\" font-weight:600; color:#080808;\">File</span><span style=\" color:#080808;\"> mode sets the tool to process a specific file individually.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.process_grp_2.setTitle(QCoreApplication.translate("DevilsRotoscope", u"Process Type", None))
#if QT_CONFIG(tooltip)
        self.ex_batch_btn.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#080808;\">Batch Processing</span></p><p><span style=\" color:#080808;\">This mode runs the tool on an entire folder structure chosen below.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ex_batch_btn.setText(QCoreApplication.translate("DevilsRotoscope", u"Batch", None))
#if QT_CONFIG(tooltip)
        self.ex_file_btn.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#080808;\">File Processing</span></p><p>This mode processes a single file.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ex_file_btn.setText(QCoreApplication.translate("DevilsRotoscope", u"File", None))
#if QT_CONFIG(tooltip)
        self.ex_folder_file_label.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#0c0c0c;\">Folder / File</span></p><p><br/></p><p><span style=\" color:#0c0c0c;\">When the </span><span style=\" font-weight:600; color:#0c0c0c;\">Process Type</span><span style=\" color:#0c0c0c;\"> is set to </span><span style=\" font-weight:600; color:#0c0c0c;\">Batch</span><span style=\" color:#0c0c0c;\">, this field takes a folder as input.  When </span><span style=\" font-weight:600; color:#0c0c0c;\">Process Type</span><span style=\" color:#0c0c0c;\"> is set to </span><span style=\" font-weight:600; color:#0c0c0c;\">File</span><span style=\" color:#0c0c0c;\">, then the field requires an existing file as its input.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ex_folder_file_label.setText(QCoreApplication.translate("DevilsRotoscope", u"Folder / File", None))
#if QT_CONFIG(tooltip)
        self.ex_folder_file.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#0c0c0c;\">Folder / File</span></p><p><br/></p><p><span style=\" color:#0c0c0c;\">When the </span><span style=\" font-weight:600; color:#0c0c0c;\">Process Type</span><span style=\" color:#0c0c0c;\"> is set to </span><span style=\" font-weight:600; color:#0c0c0c;\">Batch</span><span style=\" color:#0c0c0c;\">, this field takes a folder as input.  When </span><span style=\" font-weight:600; color:#0c0c0c;\">Process Type</span><span style=\" color:#0c0c0c;\"> is set to </span><span style=\" font-weight:600; color:#0c0c0c;\">File</span><span style=\" color:#0c0c0c;\">, then the field requires an existing file as its input.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ex_browse_btn.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#0c0c0c;\">Folder / File</span></p><p><br/></p><p><span style=\" color:#0c0c0c;\">When the </span><span style=\" font-weight:600; color:#0c0c0c;\">Process Type</span><span style=\" color:#0c0c0c;\"> is set to </span><span style=\" font-weight:600; color:#0c0c0c;\">Batch</span><span style=\" color:#0c0c0c;\">, this field takes a folder as input.  When </span><span style=\" font-weight:600; color:#0c0c0c;\">Process Type</span><span style=\" color:#0c0c0c;\"> is set to </span><span style=\" font-weight:600; color:#0c0c0c;\">File</span><span style=\" color:#0c0c0c;\">, then the field requires an existing file as its input.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ex_browse_btn.setText(QCoreApplication.translate("DevilsRotoscope", u"Browse...", None))
#if QT_CONFIG(tooltip)
        self.ex_queue_btn.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#060606;\">Load Queue</span></p><p><span style=\" color:#060606;\">This button will force an update of the selected folder or file into the Queue below</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ex_queue_btn.setText(QCoreApplication.translate("DevilsRotoscope", u"Load Queue", None))
        ___qtablewidgetitem3 = self.ex_export_table.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DevilsRotoscope", u"Original File", None));
        ___qtablewidgetitem4 = self.ex_export_table.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("DevilsRotoscope", u"Start Frame", None));
        ___qtablewidgetitem5 = self.ex_export_table.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("DevilsRotoscope", u"New Column", None));
        ___qtablewidgetitem6 = self.ex_export_table.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("DevilsRotoscope", u"First Frame Number", None));
        ___qtablewidgetitem7 = self.ex_export_table.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("DevilsRotoscope", u"Show", None));
        ___qtablewidgetitem8 = self.ex_export_table.horizontalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("DevilsRotoscope", u"Episode", None));
        ___qtablewidgetitem9 = self.ex_export_table.horizontalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("DevilsRotoscope", u"Shot Number", None));
        ___qtablewidgetitem10 = self.ex_export_table.verticalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("DevilsRotoscope", u"1", None));

        __sortingEnabled = self.ex_export_table.isSortingEnabled()
        self.ex_export_table.setSortingEnabled(False)
        ___qtablewidgetitem11 = self.ex_export_table.item(0, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("DevilsRotoscope", u"RTe", None));
        ___qtablewidgetitem12 = self.ex_export_table.item(0, 1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("DevilsRotoscope", u"sdfs", None));
        ___qtablewidgetitem13 = self.ex_export_table.item(0, 2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("DevilsRotoscope", u"sdf", None));
        ___qtablewidgetitem14 = self.ex_export_table.item(0, 3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("DevilsRotoscope", u"sdf", None));
        self.ex_export_table.setSortingEnabled(__sortingEnabled)

        self.ex_cancel_btn.setText(QCoreApplication.translate("DevilsRotoscope", u"Cancel", None))
        self.ex_run_btn.setText(QCoreApplication.translate("DevilsRotoscope", u"Export", None))
        self.toolboxes.setTabText(self.toolboxes.indexOf(self.exporter), QCoreApplication.translate("DevilsRotoscope", u"Exporter", None))
#if QT_CONFIG(tooltip)
        self.toolboxes.setTabToolTip(self.toolboxes.indexOf(self.exporter), QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#040404;\">Exporter</span></p><p><span style=\" color:#040404;\">The Exporter uses human generated data to automatically export edited clips into their respective shots within the system.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cfg_maya.setTitle(QCoreApplication.translate("DevilsRotoscope", u"Maya", None))
#if QT_CONFIG(tooltip)
        self.cfg_maya_batch_path_label.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#080808;\">Maya Batch Path</span></p><p><span style=\" color:#080808;\">The desired path to the mayabatch executable. If this file cannot be found, the system will search for a suitable replacement within the system.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cfg_maya_batch_path_label.setText(QCoreApplication.translate("DevilsRotoscope", u"Maya Batch Path", None))
#if QT_CONFIG(tooltip)
        self.cfg_maya_batch_path.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#080808;\">Maya Batch Path</span></p><p><span style=\" color:#080808;\">The desired path to the mayabatch executable. If this file cannot be found, the system will search for a suitable replacement within the system.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cfg_mayabatch_btn.setText(QCoreApplication.translate("DevilsRotoscope", u"Browse...", None))
#if QT_CONFIG(tooltip)
        self.cfg_mayapy_path_label.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#080808;\">MayaPy Path</span></p><p><span style=\" color:#080808;\">The desired path to the mayapy executable. If this file cannot be found, the system will search for a suitable replacement within the system.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cfg_mayapy_path_label.setText(QCoreApplication.translate("DevilsRotoscope", u"MayaPy Path", None))
#if QT_CONFIG(tooltip)
        self.cfg_mayapy_path.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#080808;\">MayaPy Path</span></p><p><span style=\" color:#080808;\">The desired path to the mayapy executable. If this file cannot be found, the system will search for a suitable replacement within the system.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cfg_mayapy_btn.setText(QCoreApplication.translate("DevilsRotoscope", u"Browse...", None))
        self.cfg_logger.setTitle(QCoreApplication.translate("DevilsRotoscope", u"Logging", None))
#if QT_CONFIG(tooltip)
        self.cfg_debug_logging.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#080808;\">Debug Logging</span></p><p><span style=\" color:#080808;\">Sets the logging system to record deeper debugging information.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cfg_debug_logging.setText(QCoreApplication.translate("DevilsRotoscope", u"Debug Logging", None))
#if QT_CONFIG(tooltip)
        self.cfg_num_days_logging_label.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#080808;\">Number of Days to Keep Logs</span></p><p><span style=\" color:#080808;\">The log files will cycle over time.  This will limit the number of log files kept on the system.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cfg_num_days_logging_label.setText(QCoreApplication.translate("DevilsRotoscope", u"Number of Days to Keep Logs", None))
#if QT_CONFIG(tooltip)
        self.cfg_num_days_logging.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#080808;\">Number of Days to Keep Logs</span></p><p><span style=\" color:#080808;\">The log files will cycle over time.  This will limit the number of log files kept on the system.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cfg_num_days_logging.setSpecialValueText("")
        self.cfg_mocap.setTitle(QCoreApplication.translate("DevilsRotoscope", u"Mocap", None))
#if QT_CONFIG(tooltip)
        self.cfg_default_root_label.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#080808;\">Default Root Name</span></p><p><span style=\" color:#080808;\">This is usually defined by the MoCap system, and is the name of the Root joint in an FBX.  It is usually <span style=\" font-weight:600; color:#080808;\">Root</span> or <span style=\" font-weight:600; color:#080808;\">Reference</span></span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cfg_default_root_label.setText(QCoreApplication.translate("DevilsRotoscope", u"Default Root Name", None))
#if QT_CONFIG(tooltip)
        self.cfg_default_root.setToolTip(QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#080808;\">Default Root Name</span></p><p><span style=\" color:#080808;\">This is usually defined by the MoCap system, and is the name of the Root joint in an FBX.  It is usually <span style=\" font-weight:600; color:#080808;\">Root</span> or <span style=\" font-weight:600; color:#080808;\">Reference</span></span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cfg_cancel_btn.setText(QCoreApplication.translate("DevilsRotoscope", u"Cancel", None))
        self.cfg_run_btn.setText(QCoreApplication.translate("DevilsRotoscope", u"Save/Update", None))
        self.toolboxes.setTabText(self.toolboxes.indexOf(self.config), QCoreApplication.translate("DevilsRotoscope", u"Config", None))
#if QT_CONFIG(tooltip)
        self.toolboxes.setTabToolTip(self.toolboxes.indexOf(self.config), QCoreApplication.translate("DevilsRotoscope", u"<html><head/><body><p><span style=\" font-weight:600; color:#080808;\">Config</span></p><p><span style=\" color:#080808;\">Configure the settings and variables of the tool. This can also be done in the config file.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

