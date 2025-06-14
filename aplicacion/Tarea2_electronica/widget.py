# This Python file uses the following encoding: utf-8

# from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
# from ui_form import Ui_Widget

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QStyle
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


# Ventana de informacion teorica
class InfoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = load_ui("info_window.ui")
        self.resize(800, 600)
        self.setCentralWidget(self.ui)

        # Elementos en la ventana de informacion
        self.ui.radioButton_semiconductor.clicked.connect(self.show_info)
        self.ui.radioButton_intrinseco_extrinseco.clicked.connect(self.show_info)
        self.ui.radioButton_tipon_tipop.clicked.connect(self.show_info)
        #boton atras
        self.ui.BotonAtras.setIcon(
            self.style().standardIcon(QStyle.SP_ArrowBack)  # Flecha de retroceso
        )
        self.ui.BotonAtras.clicked.connect(self.open_window)

    # funcion del boton para volver al menu principal
    def open_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.hide()

    # funcion de condicion para visualizacion de la teoria
    def show_info(self):
        if self.ui.radioButton_semiconductor.isChecked():
            self.ui.label.setText("Información de la opción 1")
        elif self.ui.radioButton_intrinseco_extrinseco.isChecked():
            self.ui.label.setText("Información de la opción 2")
        elif self.ui.radioButton_tipon_tipop.isChecked():
            self.ui.label.setText("Información de la opción 3")


# Ventana para crear iteraciones
class MathWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = load_ui("math_window.ui")
        self.resize(800, 600)
        self.setCentralWidget(self.ui)


#Elementos de la ventana de iteraciones
        #boton atras
        self.ui.BotonAtras.setIcon(
            self.style().standardIcon(QStyle.SP_ArrowBack)  # Flecha de retroceso
        )

        self.ui.BotonAtras.clicked.connect(self.open_window)
        #boton informativo
        self.ui.BotonInfo.setIcon(
                    self.style().standardIcon(QStyle.SP_MessageBoxInformation) # Ícono ⓘ estándar
                )
        self.ui.BotonInfo.setToolTip("Emplea el ensayo y error para establecer la respuesta del problema.")

    # funcion del boton para volver al menu principal
    def open_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.hide()


# Ventana del menu Principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = load_ui("main_window.ui")
        self.resize(800, 600)
        self.setCentralWidget(self.ui)

#Aqui se agrega el fondo de la ventana y se configura
        self.labelFondo = QLabel(self)
        self.labelFondo.setGeometry(0, 0, 800, 600)  # Tamaño inicial
        self.labelFondo.setPixmap(QPixmap("fondo_diodo_semiconductor.png"))
        self.labelFondo.setScaledContents(True)  # Que se escale al tamaño
        self.labelFondo.lower()  # Manda el label al fondo
        self.setMinimumSize(800, 600)

    def resizeEvent(self, event):
        self.labelFondo.resize(self.size())  # Ajusta el fondo al tamaño de la ventana
#---------------------------------------------

        self.ui.OkBoton.clicked.connect(self.open_window)
        self.ui.ExitBoton.clicked.connect(lambda: QApplication.quit())

    # Funcion para seleccionar que ventana queremos acceder
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
