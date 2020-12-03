# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'devilsRoto_pb_queuexYBLnJ.ui'
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
        Form.resize(683, 399)
        Form.setMinimumSize(QSize(683, 399))
        Form.setStyleSheet(u"background-color: rgb(100, 100, 100);\n"
"alternate-background-color: rgb(120, 120, 120);\n"
"color: rgb(230, 230, 230);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Title = QLabel(Form)
        self.Title.setObjectName(u"Title")
        self.Title.setStyleSheet(u"font: 22pt \"Tempus Sans ITC\";\n"
"color: rgb(220, 220, 220);")

        self.verticalLayout.addWidget(self.Title)

        self.playblast_queue = QTableWidget(Form)
        self.playblast_queue.setObjectName(u"playblast_queue")

        self.verticalLayout.addWidget(self.playblast_queue)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(Form)
        self.close_btn.setObjectName(u"close_btn")

        self.horizontalLayout.addWidget(self.close_btn)

        self.kill_all_btn = QPushButton(Form)
        self.kill_all_btn.setObjectName(u"kill_all_btn")

        self.horizontalLayout.addWidget(self.kill_all_btn)

        self.kill_current_btn = QPushButton(Form)
        self.kill_current_btn.setObjectName(u"kill_current_btn")

        self.horizontalLayout.addWidget(self.kill_current_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Title.setText(QCoreApplication.translate("Form", u"Devil's Rotoscope Playblast Queue", None))
        self.close_btn.setText(QCoreApplication.translate("Form", u"Close", None))
        self.kill_all_btn.setText(QCoreApplication.translate("Form", u"Kill All", None))
        self.kill_current_btn.setText(QCoreApplication.translate("Form", u"Kill Current", None))
    # retranslateUi

