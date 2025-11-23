from os import stat
from PySide6.QtGui import QIcon, QMouseEvent
from PySide6.QtWidgets import QApplication, QLabel, QSizeGrip, QWidget, QVBoxLayout
from PySide6.QtCore import Qt, QPoint
from widget_frameless.ui_wf import Ui_WidgetFrameless


class WidgetFrameless(QWidget, Ui_WidgetFrameless):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.setupUi(self)
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.drag_position = QPoint()
        self.__cnf_WidgetFrameless()

    def __cnf_WidgetFrameless(self):
        self.btn_close.clicked.connect(self.close)
        self.btn_maximize.clicked.connect(self.toggle_maximize)
        self.btn_minimize.clicked.connect(self.showMinimized)
        self.btn_lock.clicked.connect(self.toggle_on_top)
        self.btn_left.hide()
        self.btn_right.hide()
        self.lb_info.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.lb_info_aux.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.hly_bar.setContentsMargins(4,0,0,0)

        self._sizegrip = QSizeGrip(self.fr_statusbar_grip)
        self.hly_sb_grip.addWidget(self._sizegrip)
        self._szgrip_top = QSizeGrip(self.fr_btn_default)
        self.hly_btn_default.addWidget(self._szgrip_top)
        self._szgrip_no = QSizeGrip(self.fr_no)
        self.hly_no.addWidget(self._szgrip_no)

        self._load_style()
        self.set_on_top(False)

    def toggle_maximize(self):
        if self.isMaximized():
            self.showNormal()
            self.btn_maximize.setIcon(QIcon(':w-maximize.svg'))
        else:
            self.showMaximized()
            self.btn_maximize.setIcon(QIcon(':w-minimize.svg'))

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            if self.fr_bar.geometry().contains(event.pos() - self.wg_container.pos()):
                self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
        event.accept()

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if event.buttons() == Qt.LeftButton and not self.drag_position.isNull():
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.drag_position = QPoint()

    def _text_to_bar(self, wlb:QLabel, text:str, fg:str='white', append=False, bold=False):
        if bold:
            text = f'<b>{text}</b>'
        if append:
            text = self.ui.lb_info.text() + text
        wlb.setText(f'<span style=color:{fg};>{text}</span>')

    def msg(self, text:str, fg:str='white', append=False, bold=False):
        self._text_to_bar(self.lb_info, text, fg, append, bold)
        
    def msg_statusbar(self, text:str, fg:str='white', append=False, bold=False):
        self._text_to_bar(self.lb_statusbar_left, text, fg, append, bold)

    def _load_style(self):
        path_file = 'widget_frameless/styles_wf.qss'
        try:
            with open(path_file, 'r', encoding='utf-8') as f:
                style = f.read()
                self.setStyleSheet(style)
                self.msg_statusbar('style_wf.qss cargado', 'yellowgreen')
        except FileNotFoundError:
            self.msg_statusbar('styles_wf.qss no encontrado.')

    def set_on_top(self, enable:bool):
        current_flags = self.windowFlags()
        self.btn_lock.setChecked(enable)
        if enable:
            new_flags = current_flags | Qt.WindowType.WindowStaysOnTopHint
            self.msg_statusbar('enable - on top.', 'yellowgreen')
            self.btn_lock.setIcon(QIcon(':g-on-top.svg'))
        else:
            new_flags = current_flags & ~Qt.WindowType.WindowStaysOnTopHint
            self.msg_statusbar('disabled -on top', 'orange')
            self.btn_lock.setIcon(QIcon(':b-on-top.svg'))
        self.setWindowFlags(new_flags)
        self.show()

    def toggle_on_top(self):
        self.set_on_top(self.btn_lock.isChecked())


