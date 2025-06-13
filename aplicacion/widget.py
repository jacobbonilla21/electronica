# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

class InfoWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('info_window.ui', self)

        #conectar radio buttons
        self.radioButton1.clicked.connect(self.show_info)
        self.radioButton2.clicked.connect(self.show_info)
        self.radioButton3.clicked.connect(self.show_info)

    def show_info(self):
        if self.radioButton1.isChecked():
            self.label.setText("Información de la opción 1")
        elif self.radioButton2.isChecked():
            self.label.setText("Información de la opción 2")
        elif self.radioButton3.isChecked():
            self.label.setText("Información de la opción 3")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
