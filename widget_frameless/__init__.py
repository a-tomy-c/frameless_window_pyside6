from PySide6.QtGui import QMouseEvent
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
        # Conectar botones
        self.btn_close.clicked.connect(self.close)
        self.btn_maximize.clicked.connect(self.toggle_maximize)
        self.btn_minimize.clicked.connect(self.showMinimized)
        self.btn_left.hide()
        self.btn_right.hide()
        self.lb_info.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.lb_info_aux.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.hly_bar.setContentsMargins(4,0,0,0)

        self._sizegrip = QSizeGrip(self.fr_statusbar_grip)
        self.hly_sb_grip.addWidget(self._sizegrip)
        self._szgrip_top = QSizeGrip(self.fr_btn_default)
        self.hly_btn_default.addWidget(self._szgrip_top)

        self._load_style()

    def toggle_maximize(self):
        self.showNormal() if self.isMaximized() else self.showMaximized()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            # Verificar si el clic fue en la barra de título
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

    
