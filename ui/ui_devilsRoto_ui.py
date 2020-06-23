# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'devilsRoto_uiGDvYZU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(831, 695)
        Form.setStyleSheet(u"background-color: rgb(120, 120, 120);\n"
"color: rgb(220, 220, 220);")
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Title = QLabel(Form)
        self.Title.setObjectName(u"Title")
        self.Title.setStyleSheet(u"font: 22pt \"Tempus Sans ITC\";\n"
"color: rgb(220, 220, 220);")

        self.verticalLayout_3.addWidget(self.Title)

        self.toolboxes = QTabWidget(Form)
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
        self.batch_btn = QRadioButton(self.process_grp)
        self.batch_btn.setObjectName(u"batch_btn")
        self.batch_btn.setChecked(True)

        self.horizontalLayout.addWidget(self.batch_btn)

        self.file_btn = QRadioButton(self.process_grp)
        self.file_btn.setObjectName(u"file_btn")

        self.horizontalLayout.addWidget(self.file_btn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.process_grp)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.Playblaster)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(self.Playblaster)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.browse_pb_btn = QPushButton(self.Playblaster)
        self.browse_pb_btn.setObjectName(u"browse_pb_btn")

        self.horizontalLayout_2.addWidget(self.browse_pb_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.Playblaster)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.tableWidget = QTableWidget(self.Playblaster)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.cancel_btn = QPushButton(self.Playblaster)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout_3.addWidget(self.cancel_btn)

        self.run_btn = QPushButton(self.Playblaster)
        self.run_btn.setObjectName(u"run_btn")

        self.horizontalLayout_3.addWidget(self.run_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.toolboxes.addTab(self.Playblaster, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.toolboxes.addTab(self.tab_2, "")

        self.verticalLayout_3.addWidget(self.toolboxes)


        self.retranslateUi(Form)

        self.toolboxes.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Title.setText(QCoreApplication.translate("Form", u"Devil's Rotoscope tools", None))
        self.process_grp.setTitle(QCoreApplication.translate("Form", u"Process Type", None))
        self.batch_btn.setText(QCoreApplication.translate("Form", u"Batch", None))
        self.file_btn.setText(QCoreApplication.translate("Form", u"File", None))
        self.label.setText(QCoreApplication.translate("Form", u"Folder / File", None))
        self.browse_pb_btn.setText(QCoreApplication.translate("Form", u"Browse...", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Playblast Queue", None))
        self.cancel_btn.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.run_btn.setText(QCoreApplication.translate("Form", u"Run Playblasts", None))
        self.toolboxes.setTabText(self.toolboxes.indexOf(self.Playblaster), QCoreApplication.translate("Form", u"Playblaster", None))
        self.toolboxes.setTabText(self.toolboxes.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Tab 2", None))
    # retranslateUi

