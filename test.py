import sys
from PySide6.QtWidgets import QApplication
from widget_frameless import WidgetFrameless


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wf = WidgetFrameless()
    wf.set_title(' Mi PROGRAMA ', fg='black', bg='skyblue')
    wf.set_text_info('Archivo creado: ')
    wf.set_text_info('mi archivo.txt', 'yellow', append=True, bold=True)
    wf.set_text_info_aux('.TXT', 'orange', bold=True)
    wf.msg_statusbar('configuraciones cargadas.', 'yellowgreen')
    wf.msg_statusbar_right('error superdesastrozo.', '#E15F6E', bold=True)
    wf.msg_statusbar_right(' pedazo de ...', 'azure', append=True)
    
    wf.show()
    sys.exit(app.exec())
    
