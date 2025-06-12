# This Python file uses the following encoding: utf-8

# from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
# from ui_form import Ui_Widget

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
import sys

loader = QUiLoader()


def load_ui(ui_file):
    file = QFile(ui_file)
    if not file.open(QIODevice.ReadOnly):
        print(f"No se pudo abrir {ui_file}")
        return None
    window = loader.load(file)
    file.close()
    return window


class InfoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = load_ui("info_window.ui")
        self.setCentralWidget(self.ui)

        self.ui.radioButton_semiconductor.clicked.connect(self.show_info)
        self.ui.radioButton_intrinseco_extrinseco.clicked.connect(self.show_info)
        self.ui.radioButton_tipon_tipop.clicked.connect(self.show_info)

    def show_info(self):
        if self.ui.radioButton_semiconductor.isChecked():
            self.ui.label.setText("Información de la opción 1")
        elif self.ui.radioButton_intrinseco_extrinseco.isChecked():
            self.ui.label.setText("Información de la opción 2")
        elif self.ui.radioButton_tipon_tipop.isChecked():
            self.ui.label.setText("Información de la opción 3")


class MathWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = load_ui("math_window.ui")
        self.setCentralWidget(self.ui)


#         self.ui.pushButtonSumar.clicked.connect(self.sumar)
#         self.ui.pushButtonRestar.clicked.connect(self.restar)
#         self.ui.pushButtonMultiplicar.clicked.connect(self.multiplicar)
#         self.ui.pushButtonDividir.clicked.connect(self.dividir)
#
#     def get_values(self):
#         try:
#             a = float(self.ui.lineEdit1.text())
#             b = float(self.ui.lineEdit2.text())
#             return a, b
#         except ValueError:
#             self.ui.labelResultado.setText("Entrada inválida")
#             return None, None
#
#     def sumar(self):
#         a, b = self.get_values()
#         if a is not None:
#             self.ui.labelResultado.setText(str(a + b))
#
#     def restar(self):
#         a, b = self.get_values()
#         if a is not None:
#             self.ui.labelResultado.setText(str(a - b))
#
#     def multiplicar(self):
#         a, b = self.get_values()
#         if a is not None:
#             self.ui.labelResultado.setText(str(a * b))
#
#     def dividir(self):
#         a, b = self.get_values()
#         if a is not None:
#             if b != 0:
#                 self.ui.labelResultado.setText(str(a / b))
#             else:
#                 self.ui.labelResultado.setText("Error: División por cero")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = load_ui("main_window.ui")
        self.setCentralWidget(self.ui)

        self.ui.OkBoton.clicked.connect(self.open_window)

    def open_window(self):
        opcion = self.ui.Seleccion_menu.currentIndex()
        if opcion == 0:
            self.info_window = InfoWindow()
            self.info_window.show()
        elif opcion == 1:
            self.math_window = MathWindow()
            self.math_window.show()


# class Widget(QWidget):
#    def __init__(self, parent=None):
#        super().__init__(parent)
#        self.ui = Ui_Widget()
#        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
