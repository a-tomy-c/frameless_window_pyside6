import sys
from PySide6.QtWidgets import QApplication
from widget_frameless import WidgetFrameless


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wf = WidgetFrameless()
    wf.show()
    sys.exit(app.exec())
    
