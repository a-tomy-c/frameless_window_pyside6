from os import stat
from PySide6.QtGui import QIcon, QMouseEvent, QWindow
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

        self._szgrip_se = QSizeGrip(self.fr_grip_se)
        self.hly_sb_grip_se.addWidget(self._szgrip_se)
        self._szgrip_ne = QSizeGrip(self.fr_btn_default)
        self.hly_btn_default.addWidget(self._szgrip_ne)
        self._szgrip_no = QSizeGrip(self.fr_grip_no)
        self.hly_grip_no.addWidget(self._szgrip_no)
        self._szgrip_so = QSizeGrip(self.fr_grip_so)
        self.hly_sb_grip_so.addWidget(self._szgrip_so)

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
            text = wlb.text() + text
        wlb.setText(f'<span style=color:{fg};>{text}</span>')
        
    def msg_statusbar(self, text:str, fg:str='white', append=False, bold=False):
        """asigna texto a la statusbar a la izquierda"""
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

    def set_title(self, text:str, fg:str, bg:str):
        """asigna titulo"""
        self.btn_title.setText(text)
        self.btn_title.setStyleSheet(f'color:{fg}; background-color:{bg};')
        self.btn_title.setMinimumWidth(len(text)*8)

    def set_icon(self, icon:str):
        """asigna icono al boton icono"""
        self.btn_logo.setIcon(QIcon(icon))

    def set_text_info_aux(self, text:str, fg:str='white', append=False, bold=False):
        """asigna texto a la barra de titulo a la derecha"""
        self._text_to_bar(self.lb_info_aux, text, fg, append, bold)
        self.lb_info_aux.setMaximumWidth(len(text)*8)

    def set_text_info(self, text:str, fg:str='white', append=False, bold=False):
        """asigna texto a la barra de titulo a la izquierda"""
        self._text_to_bar(self.lb_info, text, fg, append, bold)

    def msg_statusbar_right(self, text:str, fg:str='white', append=False, bold=False):
        """asigna texto a la statusbar a la derecha"""
        self._text_to_bar(self.lb_statusbar_right, text, fg, append, bold)

    def add_widget(self, widget:QWidget):
        """agregar widget a la ventana"""
        self.vly_body.addWidget(widget)

    def add_to_statusbar_left(self, widget:QWidget):
        """agregar widget al statusbar IZQUIERDA"""
        self.hly_sb_left.addWidget(widget)
        
    def add_to_statusbar_mid(self, widget:QWidget):
        """agregar widget al statusbar MEDIO"""
        self.hly_sb_mid.addWidget(widget)
        
    def add_to_statusbar_right(self, widget:QWidget):
        """agregar widget al statusbar DERECHA"""
        self.hly_sb_right.addWidget(widget)
    
