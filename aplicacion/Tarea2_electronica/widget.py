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

#Ventana de informacion teorica
class InfoWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = load_ui("info_window.ui")
        self.resize(800,600)
        self.setCentralWidget(self.ui)


#Elementos en la ventana de informacion
        self.ui.radioButton_semiconductor.clicked.connect(self.show_info)
        self.ui.radioButton_intrinseco_extrinseco.clicked.connect(self.show_info)
        self.ui.radioButton_tipon_tipop.clicked.connect(self.show_info)
        self.ui.BotonAtras.clicked.connect(self.open_window)

#funcion del boton para volver al menu principal
    def open_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.hide()

    #funcion de condicion para visualizacion de la teoria
    def show_info(self):
        if self.ui.radioButton_semiconductor.isChecked():
            self.ui.label.setText("Información de la opción 1")
        elif self.ui.radioButton_intrinseco_extrinseco.isChecked():
            self.ui.label.setText("Información de la opción 2")
        elif self.ui.radioButton_tipon_tipop.isChecked():
            self.ui.label.setText("Información de la opción 3")

#Ventana para crear iteraciones
class MathWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = load_ui("math_window.ui")
        self.resize(800,600)
        self.setCentralWidget(self.ui)

#Elementos de la ventana de iteraciones
        self.ui.BotonAtras.clicked.connect(self.open_window)

#funcion del boton para volver al menu principal
    def open_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.hide()

#Ventana del menu Principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = load_ui("main_window.ui")
        self.resize(800,600)
        self.setCentralWidget(self.ui)

        self.ui.OkBoton.clicked.connect(self.open_window)

#Funcion para seleccionar que ventana queremos acceder
    def open_window(self):
        opcion = self.ui.Seleccion_menu.currentIndex()
        if opcion == 1:
            self.info_window = InfoWindow()
            self.hide()
            self.info_window.show()
        elif opcion == 2:
            self.math_window = MathWindow()
            self.hide()
            self.math_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
