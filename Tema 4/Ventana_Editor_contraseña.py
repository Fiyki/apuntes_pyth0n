from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget
import Editor_Contraseñas


class VentanaConfiguracion(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contraseñas")
        self.setGeometry(125, 125, 350, 50)

        # Creamos una instancia del editor de contraseña
        self.editor_contrasena = Editor_Contraseñas.EditorContraseña(self)

        # Configuramos el diseño de la ventana
        layout = QVBoxLayout()
        layout.addWidget(self.editor_contrasena)
        self.setLayout(layout)


if __name__ == "__main__":
    import os

    app = QApplication([])

    # Creamos una instancia de la ventana de configuración
    ventana_configuracion = VentanaConfiguracion()

    # Llamamos a cambiar_visibilidad() después de que la ventana sea mostrada
    ventana_configuracion.show()
    ventana_configuracion.editor_contrasena.cambiar_visibilidad()

    app.exec()
