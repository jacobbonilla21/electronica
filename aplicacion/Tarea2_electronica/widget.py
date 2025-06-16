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
from PySide6.QtGui import QPixmap, QDoubleValidator
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem, QStyle
from PySide6.QtCore import Qt
import numpy as np
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
            self.ui.label_info.setText("<h2>🔌 Conductor, Aislante y Semiconductor</h2>"
            "<ul>"
            "<li><b>Conductor:</b> Permite el flujo de corriente fácilmente. Ej: cobre, oro.</li>"
            "<li><b>Aislante:</b> No permite el paso de corriente. Ej: vidrio, plástico.</li>"
            "<li><b>Semiconductor:</b> Puede comportarse como conductor o aislante según condiciones.</li>"
            "</ul>"
            "<br>"
            "<img src='diferencia_conductor_semicondutor_aislante.jpg' style='max-width:100%; height:auto;'")

        elif self.ui.radioButton_intrinseco_extrinseco.isChecked():
            self.ui.label_info.setText("<h2>🔬 Intrínseco vs Extrínseco</h2>"
            "<ul>"
            "<li><b>Intrínseco:</b> Puro, solo átomos iguales (como silicio puro).</li>"
            "<li><b>Extrínseco:</b> Dopado con impurezas para mejorar la conductividad.</li>"
            "</ul>"
            "<br>"
            "<img src='semiconductores_extrinsecos.jpg' style='max-width:100%; height:auto;'"
            "<br>"
            "<img src='semiconductores_intrinseco.jpg' style='max-width:100%; margin-top:1; height:auto;'"
            )

        elif self.ui.radioButton_tipon_tipop.isChecked():
            self.ui.label_info.setText("<h2>🧪 Tipo n vs Tipo p</h2>"
            "<ul>"
            "<li><b>Tipo n:</b> Dopado con átomos con más electrones (como fósforo).</li>"
            "<li><b>Tipo p:</b> Dopado con átomos con menos electrones (como boro).</li>"
            "</ul>"
            "<br>"
            "<img src='materiales_tipon_tipop.jpg' style='max-width:100%; height:auto;'")


# Ventana para crear iteraciones
class MathWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = load_ui("math_window.ui")
        self.resize(800, 635)
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

        # Primero conectar TODOS los botones
        self.ui.btnLimpiar.clicked.connect(self.limpiar_campos)
        self.ui.btnCalcular.clicked.connect(self.calcular)

        # Luego configurar el resto
        self.setup_ui()

    # funcion del boton para volver al menu principal
    def open_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.hide()

    def setup_ui(self):
        # Configurar validación para campos QLineEdit (notación científica)
        scientific_validator = QDoubleValidator()
        scientific_validator.setNotation(QDoubleValidator.ScientificNotation)
        self.ui.inputIs.setValidator(scientific_validator)
        self.ui.inputID.setValidator(QDoubleValidator(0.0001, 1000, 4))

    def limpiar_campos(self):
        """Limpia todos los campos pero mantiene los encabezados de la tabla con formato"""
        try:
            # 1. Reiniciar valores de los inputs
            self.ui.inputVSS.setValue(0.0)
            self.ui.inputR.setValue(0.0)
            self.ui.inputN.setValue(1.0)  # Valor por defecto para n
            self.ui.inputVD.setValue(0.7)  # Valor por defecto para v_D

            # 2. Limpiar campos de texto
            self.ui.inputIs.clear()
            self.ui.inputID.clear()

            # 3. Limpiar el contenido de la tabla PERO MANTENER ENCABEZADOS
            self.ui.tablaResultados.clearContents()  # Limpia solo el contenido
            self.ui.tablaResultados.setRowCount(0)   # Elimina todas las filas

            # 4. Limpiar el label de resultado
            self.ui.labelResultado.clear()

            # 5. Fuerza actualización visual
            self.ui.tablaResultados.viewport().update()

            # 6. Mostrar mensaje de éxito (mismo estilo que tus errores)
            QMessageBox.information(
                self,
                "Campos limpiados",
                "Todos los campos han sido restablecidos\n"
                "a sus valores por defecto correctamente."
            )

        except Exception as e:
            QMessageBox.critical(
                self,
                "Error al limpiar",
                f"No se pudieron restablecer los campos:\n{str(e)}"
            )

    def calcular(self):
        try:
            # Obtener valores de los inputs
            V_SS = self.ui.inputVSS.value()
            R = self.ui.inputR.value()
            n = self.ui.inputN.value()
            v_D = self.ui.inputVD.value()

            # Manejar I_s e i_D (campos opcionales)
            I_s = float(self.ui.inputIs.text()) if self.ui.inputIs.text() else None
            i_D = float(self.ui.inputID.text()) if self.ui.inputID.text() else None

            # Validaciones básicas
            if R <= 0 or V_SS <= 0:
                raise ValueError("R y Vss deben ser mayor a cero")
            if I_s is None and i_D is None:
                raise ValueError("Ingresa Is o iD inicial")

            print(f"Vss = ",V_SS)
            print(f"R = ",R)
            print(f"n = ",n)
            print(f"vD = ",v_D)
            print(f"iD = ",i_D)
            print(f"Is = ",I_s)

            # Calcular iteraciones
            resultados = self.calcular_iteraciones(V_SS, R, n, I_s, i_D, v_D)
            self.mostrar_resultados(resultados)

        except ValueError as e:
            QMessageBox.critical(self, "Error", f"Datos inválidos:\n{str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error inesperado:\n{str(e)}")

    def calcular_iteraciones(self, V_SS, R, n, I_s, i_D, v_D, iteraciones=5):
        V_T = 0.026
        factor = 0.1 if n == 1 else 2.3 * n * V_T

        print(f"factor: ",factor)
        # Asegurar que I_s esté en mA (si es muy pequeño, se asume en A)
        if I_s is not None:
            if I_s >= 1e-3:  # Si I_s es >= 1mA, convertir a mA
                I_s /= 1000  # A → mA
            # Nota: Si I_s es 1e-12 (típico en diodos), se queda igual (ya es mA-equivalente)

        # 1. Calcular corriente inicial si no se proporciona
        if i_D is None:
            i_D = (I_s * np.exp(v_D / (n * V_T)))*1000

        # 2. Inicializar listas para almacenar resultados
        resultados = [('Inicial', v_D, i_D)]  # Valores iniciales (no son iteración)

        ## 3. Realizar iteraciones (comenzando desde 1 hasta el número solicitado)
        v_actual = v_D
        i_actual = i_D

        for k in range(1, iteraciones + 1):
            # Calcular nueva corriente: iD_k = (V_SS - v_actual)/R
            i_nueva = ((V_SS - v_actual) / R)* 1000  # Convertir (V_SS - vD)/R → mA

            # Calcular nuevo voltaje: vD_k = v_actual + factor * log(i_nueva/i_actual)
            if i_nueva > 1e-12 and i_actual > 1e-12:  # Evitar log(0)
                ratio = i_nueva / i_actual
                v_nueva = v_actual + factor * np.log10(ratio)
            else:
                v_nueva = v_actual  # Mantener valor anterior si hay problema

            # Guardar esta iteración
            resultados.append((k, v_nueva, i_nueva))

            # Actualizar valores para la próxima iteración
            v_actual = v_nueva
            i_actual = i_nueva

        # 4. Debug: Imprimir resultados
        print("\n" + "="*50)
        print("RESULTADOS ITERATIVOS")
        print("="*50)
        for iter_num, vD, iD in resultados:
            if iter_num == 'Inicial':
                print(f"Valores iniciales: vD = {vD:.6f} V, iD = {iD:.6f} A")
            else:
                print(f"Iteración {iter_num}: vD = {vD:.6f} V, iD = {iD:.6f} A")
            print(f"  Verificación: (Vss - vD)/R = {(V_SS - vD)/R:.6f} A")

        return resultados

    def mostrar_resultados(self, resultados):
        # Configurar tabla
        self.ui.tablaResultados.setRowCount(0)
        self.ui.tablaResultados.setColumnCount(3)
        self.ui.tablaResultados.setHorizontalHeaderLabels(["Iteración", "vD (V)", "iD (mA)"])

        # Llenar tabla
        for k, v_D, i_D in resultados:
            row = self.ui.tablaResultados.rowCount()
            self.ui.tablaResultados.insertRow(row)
            # Crear items y centrarlos
            item_iter = QTableWidgetItem(str(k))
            item_iter.setTextAlignment(Qt.AlignCenter)  # <-- Centrar

            item_vd = QTableWidgetItem(f"{v_D:.4g}")
            item_vd.setTextAlignment(Qt.AlignCenter)  # <-- Centrar

            item_id = QTableWidgetItem(f"{i_D:.4g}")
            item_id.setTextAlignment(Qt.AlignCenter)  # <-- Centrar

            # Añadir items a la tabla
            self.ui.tablaResultados.setItem(row, 0, item_iter)
            self.ui.tablaResultados.setItem(row, 1, item_vd)
            self.ui.tablaResultados.setItem(row, 2, item_id)

        # Mostrar resultado final
        v_final, i_final = resultados[-1][1], resultados[-1][2]
        self.ui.labelResultado.setText(
            f"<b>Resultado final:</b><br>"
            f"v<sub>D</sub> = {v_final:.4g} V<br>"
            f"i<sub>D</sub> = {i_final:.4g} mA"
        )

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
