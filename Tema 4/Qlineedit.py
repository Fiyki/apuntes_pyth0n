import sys

from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QWidget, QLineEdit, QLabel, QApplication


class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo qtlineedit")
        self.setFixedSize(300, 30)
        self.mostrar = QIcon("C:/Users/danmo\OneDrive/Escritorio/Dam 2/Desarrollo de interfaces/DesarrolloInterfaces_python1/Tema 3/iconos/DI_U04_A01_PP_E_1.png")  # Necesitas proporcionar el path del ícono
        self.line_edit1 = QLineEdit(self)

        # Fijamos el tamaño del line edit
        self.line_edit1.setFixedSize(150, 30)
        self.line_edit1.setMaxLength(25)

        # Crear la acción y conectarla al slot cambiar visibilidad
        self.accion_cambiar_visibilidad = QAction(self.mostrar, "ejemplo", self)
        self.accion_cambiar_visibilidad.triggered.connect(self.cambiar_visibilidad)

        # Agregar la acción al QLineEdit
        self.line_edit1.addAction(self.accion_cambiar_visibilidad, QLineEdit.TrailingPosition)

        self.etiqueta1 = QLabel(self)
        self.etiqueta1.setFixedSize(150, 30)
        self.etiqueta1.move(150, 0)

        # Conectamos el evento textChanged del LineEdit al slot setText del Label
        self.line_edit1.textChanged.connect(self.etiqueta1.setText)

    def cambiar_visibilidad(self):
        print("Yindiii")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())  # Agregado sys.exit para manejar correctamente la salida del programa
