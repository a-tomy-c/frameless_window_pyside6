# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_frameless.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import widget_frameless.icons.icons_wf

class Ui_WidgetFrameless(object):
    def setupUi(self, WidgetFrameless):
        if not WidgetFrameless.objectName():
            WidgetFrameless.setObjectName(u"WidgetFrameless")
        WidgetFrameless.resize(669, 504)
        self.vly_wf = QVBoxLayout(WidgetFrameless)
        self.vly_wf.setSpacing(0)
        self.vly_wf.setObjectName(u"vly_wf")
        self.vly_wf.setContentsMargins(0, 0, 0, 0)
        self.wg_container = QWidget(WidgetFrameless)
        self.wg_container.setObjectName(u"wg_container")
        self.vly_container = QVBoxLayout(self.wg_container)
        self.vly_container.setSpacing(0)
        self.vly_container.setObjectName(u"vly_container")
        self.vly_container.setContentsMargins(2, 0, 2, 2)
        self.vly_in_container = QVBoxLayout()
        self.vly_in_container.setSpacing(0)
        self.vly_in_container.setObjectName(u"vly_in_container")
        self.fr_bar = QFrame(self.wg_container)
        self.fr_bar.setObjectName(u"fr_bar")
        self.fr_bar.setMinimumSize(QSize(0, 20))
        self.fr_bar.setMaximumSize(QSize(16777215, 20))
        self.fr_bar.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_bar.setFrameShadow(QFrame.Shadow.Plain)
        self.hly_fr_bar = QHBoxLayout(self.fr_bar)
        self.hly_fr_bar.setSpacing(0)
        self.hly_fr_bar.setObjectName(u"hly_fr_bar")
        self.hly_fr_bar.setContentsMargins(0, 0, 0, 0)
        self.hly_bar = QHBoxLayout()
        self.hly_bar.setSpacing(0)
        self.hly_bar.setObjectName(u"hly_bar")
        self.btn_logo = QPushButton(self.fr_bar)
        self.btn_logo.setObjectName(u"btn_logo")
        self.btn_logo.setMinimumSize(QSize(20, 20))
        self.btn_logo.setMaximumSize(QSize(20, 20))
        icon = QIcon()
        icon.addFile(u":/tw.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_logo.setIcon(icon)
        self.btn_logo.setIconSize(QSize(20, 20))
        self.btn_logo.setFlat(True)

        self.hly_bar.addWidget(self.btn_logo)

        self.btn_title = QPushButton(self.fr_bar)
        self.btn_title.setObjectName(u"btn_title")
        self.btn_title.setMinimumSize(QSize(0, 20))
        self.btn_title.setMaximumSize(QSize(80, 20))
        self.btn_title.setIconSize(QSize(24, 24))
        self.btn_title.setFlat(True)

        self.hly_bar.addWidget(self.btn_title)

        self.btn_lock = QPushButton(self.fr_bar)
        self.btn_lock.setObjectName(u"btn_lock")
        self.btn_lock.setMinimumSize(QSize(25, 20))
        self.btn_lock.setMaximumSize(QSize(25, 20))
        icon1 = QIcon()
        icon1.addFile(u":/w-on-top.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_lock.setIcon(icon1)
        self.btn_lock.setIconSize(QSize(16, 16))
        self.btn_lock.setFlat(True)

        self.hly_bar.addWidget(self.btn_lock)

        self.btn_left = QPushButton(self.fr_bar)
        self.btn_left.setObjectName(u"btn_left")
        self.btn_left.setMinimumSize(QSize(30, 20))
        self.btn_left.setMaximumSize(QSize(30, 20))
        self.btn_left.setIconSize(QSize(24, 24))
        self.btn_left.setFlat(True)

        self.hly_bar.addWidget(self.btn_left)

        self.lb_info = QLabel(self.fr_bar)
        self.lb_info.setObjectName(u"lb_info")
        self.lb_info.setMaximumSize(QSize(16777215, 20))

        self.hly_bar.addWidget(self.lb_info)

        self.lb_info_aux = QLabel(self.fr_bar)
        self.lb_info_aux.setObjectName(u"lb_info_aux")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_info_aux.sizePolicy().hasHeightForWidth())
        self.lb_info_aux.setSizePolicy(sizePolicy)
        self.lb_info_aux.setMaximumSize(QSize(16777215, 20))

        self.hly_bar.addWidget(self.lb_info_aux)

        self.btn_right = QPushButton(self.fr_bar)
        self.btn_right.setObjectName(u"btn_right")
        self.btn_right.setMinimumSize(QSize(30, 20))
        self.btn_right.setMaximumSize(QSize(30, 20))
        self.btn_right.setIconSize(QSize(24, 24))
        self.btn_right.setFlat(True)

        self.hly_bar.addWidget(self.btn_right)

        self.fr_btn_default = QFrame(self.fr_bar)
        self.fr_btn_default.setObjectName(u"fr_btn_default")
        self.fr_btn_default.setMinimumSize(QSize(80, 0))
        self.fr_btn_default.setMaximumSize(QSize(85, 16777215))
        self.fr_btn_default.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_btn_default.setFrameShadow(QFrame.Shadow.Plain)
        self.fr_btn_default.setLineWidth(0)
        self.hly_btn_default = QHBoxLayout(self.fr_btn_default)
        self.hly_btn_default.setSpacing(0)
        self.hly_btn_default.setObjectName(u"hly_btn_default")
        self.hly_btn_default.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.fr_btn_default)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(30, 20))
        self.btn_minimize.setMaximumSize(QSize(30, 20))
        icon2 = QIcon()
        icon2.addFile(u":/w-min.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_minimize.setIcon(icon2)
        self.btn_minimize.setIconSize(QSize(18, 18))
        self.btn_minimize.setFlat(True)

        self.hly_btn_default.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.fr_btn_default)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(30, 20))
        self.btn_maximize.setMaximumSize(QSize(30, 20))
        icon3 = QIcon()
        icon3.addFile(u":/w-maximize.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_maximize.setIcon(icon3)
        self.btn_maximize.setIconSize(QSize(16, 16))
        self.btn_maximize.setFlat(True)

        self.hly_btn_default.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.fr_btn_default)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(25, 20))
        self.btn_close.setMaximumSize(QSize(20, 20))
        icon4 = QIcon()
        icon4.addFile(u":/w-close.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_close.setIcon(icon4)
        self.btn_close.setIconSize(QSize(18, 18))
        self.btn_close.setFlat(True)

        self.hly_btn_default.addWidget(self.btn_close)


        self.hly_bar.addWidget(self.fr_btn_default)


        self.hly_fr_bar.addLayout(self.hly_bar)


        self.vly_in_container.addWidget(self.fr_bar)

        self.sw = QStackedWidget(self.wg_container)
        self.sw.setObjectName(u"sw")
        self.page_0 = QWidget()
        self.page_0.setObjectName(u"page_0")
        self.vly_page_0 = QVBoxLayout(self.page_0)
        self.vly_page_0.setSpacing(0)
        self.vly_page_0.setObjectName(u"vly_page_0")
        self.vly_page_0.setContentsMargins(0, 0, 0, 0)
        self.vly_body = QVBoxLayout()
        self.vly_body.setSpacing(4)
        self.vly_body.setObjectName(u"vly_body")
        self.vly_body.setContentsMargins(2, 2, 2, 2)

        self.vly_page_0.addLayout(self.vly_body)

        self.sw.addWidget(self.page_0)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.vly_page_1 = QVBoxLayout(self.page_1)
        self.vly_page_1.setSpacing(0)
        self.vly_page_1.setObjectName(u"vly_page_1")
        self.vly_page_1.setContentsMargins(0, 0, 0, 0)
        self.vly_body_aux = QVBoxLayout()
        self.vly_body_aux.setObjectName(u"vly_body_aux")

        self.vly_page_1.addLayout(self.vly_body_aux)

        self.sw.addWidget(self.page_1)

        self.vly_in_container.addWidget(self.sw)

        self.fr_status_bar = QFrame(self.wg_container)
        self.fr_status_bar.setObjectName(u"fr_status_bar")
        self.fr_status_bar.setMinimumSize(QSize(0, 20))
        self.fr_status_bar.setMaximumSize(QSize(16777215, 20))
        self.fr_status_bar.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_status_bar.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.fr_status_bar)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.wg_status_bar = QWidget(self.fr_status_bar)
        self.wg_status_bar.setObjectName(u"wg_status_bar")
        self.wg_status_bar.setMaximumSize(QSize(16777215, 20))
        self.vly_wg_status_bar = QVBoxLayout(self.wg_status_bar)
        self.vly_wg_status_bar.setObjectName(u"vly_wg_status_bar")
        self.vly_wg_status_bar.setContentsMargins(0, 0, 0, 0)
        self.hly_status_bar = QHBoxLayout()
        self.hly_status_bar.setObjectName(u"hly_status_bar")
        self.fr_statusbar_left = QFrame(self.wg_status_bar)
        self.fr_statusbar_left.setObjectName(u"fr_statusbar_left")
        self.fr_statusbar_left.setMaximumSize(QSize(16777215, 20))
        self.fr_statusbar_left.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_statusbar_left.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout = QVBoxLayout(self.fr_statusbar_left)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.hly_sb_left = QHBoxLayout()
        self.hly_sb_left.setObjectName(u"hly_sb_left")

        self.verticalLayout.addLayout(self.hly_sb_left)


        self.hly_status_bar.addWidget(self.fr_statusbar_left)

        self.lb_statusbar_left = QLabel(self.wg_status_bar)
        self.lb_statusbar_left.setObjectName(u"lb_statusbar_left")
        self.lb_statusbar_left.setMaximumSize(QSize(16777215, 20))

        self.hly_status_bar.addWidget(self.lb_statusbar_left)

        self.horizontalSpacer_sb0 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hly_status_bar.addItem(self.horizontalSpacer_sb0)

        self.fr_statusbar_mid = QFrame(self.wg_status_bar)
        self.fr_statusbar_mid.setObjectName(u"fr_statusbar_mid")
        self.fr_statusbar_mid.setMaximumSize(QSize(16777215, 20))
        self.fr_statusbar_mid.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_statusbar_mid.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.fr_statusbar_mid)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.hly_sb_mid = QHBoxLayout()
        self.hly_sb_mid.setObjectName(u"hly_sb_mid")

        self.verticalLayout_2.addLayout(self.hly_sb_mid)


        self.hly_status_bar.addWidget(self.fr_statusbar_mid)

        self.horizontalSpacer_sb1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hly_status_bar.addItem(self.horizontalSpacer_sb1)

        self.lb_statusbar_right = QLabel(self.wg_status_bar)
        self.lb_statusbar_right.setObjectName(u"lb_statusbar_right")
        self.lb_statusbar_right.setMaximumSize(QSize(16777215, 20))
        self.lb_statusbar_right.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.hly_status_bar.addWidget(self.lb_statusbar_right)

        self.fr_statusbar_grip = QFrame(self.wg_status_bar)
        self.fr_statusbar_grip.setObjectName(u"fr_statusbar_grip")
        self.fr_statusbar_grip.setMaximumSize(QSize(16777215, 20))
        self.fr_statusbar_grip.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_statusbar_grip.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.fr_statusbar_grip)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.hly_sb_grip = QHBoxLayout()
        self.hly_sb_grip.setSpacing(0)
        self.hly_sb_grip.setObjectName(u"hly_sb_grip")

        self.verticalLayout_3.addLayout(self.hly_sb_grip)


        self.hly_status_bar.addWidget(self.fr_statusbar_grip)

        self.fr_statusbar_right = QFrame(self.wg_status_bar)
        self.fr_statusbar_right.setObjectName(u"fr_statusbar_right")
        self.fr_statusbar_right.setMaximumSize(QSize(16777215, 20))
        self.fr_statusbar_right.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_statusbar_right.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.fr_statusbar_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.hly_sb_right = QHBoxLayout()
        self.hly_sb_right.setObjectName(u"hly_sb_right")

        self.verticalLayout_4.addLayout(self.hly_sb_right)


        self.hly_status_bar.addWidget(self.fr_statusbar_right)


        self.vly_wg_status_bar.addLayout(self.hly_status_bar)


        self.verticalLayout_5.addWidget(self.wg_status_bar)


        self.vly_in_container.addWidget(self.fr_status_bar)


        self.vly_container.addLayout(self.vly_in_container)


        self.vly_wf.addWidget(self.wg_container)


        self.retranslateUi(WidgetFrameless)

        self.btn_logo.setDefault(False)


        QMetaObject.connectSlotsByName(WidgetFrameless)
    # setupUi

    def retranslateUi(self, WidgetFrameless):
        WidgetFrameless.setWindowTitle(QCoreApplication.translate("WidgetFrameless", u"Form", None))
        self.btn_logo.setText("")
        self.btn_title.setText(QCoreApplication.translate("WidgetFrameless", u"FRAMELESS", None))
        self.btn_lock.setText("")
        self.btn_left.setText("")
        self.lb_info.setText("")
        self.lb_info_aux.setText("")
        self.btn_right.setText("")
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.lb_statusbar_left.setText("")
        self.lb_statusbar_right.setText("")
    # retranslateUi

