# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_about.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)
import widget_frameless.icons.icons_wf

class Ui_DialogAbout(object):
    def setupUi(self, DialogAbout):
        if not DialogAbout.objectName():
            DialogAbout.setObjectName(u"DialogAbout")
        DialogAbout.resize(491, 228)
        self.verticalLayout_3 = QVBoxLayout(DialogAbout)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lb_logo = QLabel(DialogAbout)
        self.lb_logo.setObjectName(u"lb_logo")
        self.lb_logo.setMinimumSize(QSize(150, 150))

        self.verticalLayout_2.addWidget(self.lb_logo)

        self.lb_aux = QLabel(DialogAbout)
        self.lb_aux.setObjectName(u"lb_aux")

        self.verticalLayout_2.addWidget(self.lb_aux)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_title = QLabel(DialogAbout)
        self.lb_title.setObjectName(u"lb_title")
        font = QFont()
        font.setPointSize(14)
        self.lb_title.setFont(font)

        self.verticalLayout.addWidget(self.lb_title)

        self.te_info = QTextEdit(DialogAbout)
        self.te_info.setObjectName(u"te_info")
        self.te_info.setFrameShape(QFrame.Shape.NoFrame)
        self.te_info.setFrameShadow(QFrame.Shadow.Plain)
        self.te_info.setReadOnly(True)

        self.verticalLayout.addWidget(self.te_info)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.retranslateUi(DialogAbout)

        QMetaObject.connectSlotsByName(DialogAbout)
    # setupUi

    def retranslateUi(self, DialogAbout):
        DialogAbout.setWindowTitle(QCoreApplication.translate("DialogAbout", u"Dialog", None))
        self.lb_logo.setText("")
        self.lb_aux.setText("")
        self.lb_title.setText(QCoreApplication.translate("DialogAbout", u"MIRA PLAYER CHAPTERS", None))
    # retranslateUi

