import os

from PySide6.QtGui import QIcon, QKeySequence
from PySide6.QtWidgets import QLineEdit


class EditorContraseña(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Obtenemos la ruta del directorio actual del script
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Rutas relativas a los iconos
        mostrar_icon_path = os.path.join(current_directory, "verde.png")
        ocultar_icon_path = os.path.join(current_directory, "rojo.png")

        # Verificar si los archivos de íconos existen
        if os.path.exists(mostrar_icon_path) and os.path.exists(ocultar_icon_path):
            self.mostrar = QIcon(mostrar_icon_path)
            self.ocultar = QIcon(ocultar_icon_path)
        else:
            raise FileNotFoundError("No se pueden encontrar los archivos de íconos.")

        self.setEchoMode(QLineEdit.EchoMode.Password)
        self.setPlaceholderText("Introduce tu contraseña")

        self.accion_cambiar_visibilidad = self.addAction(self.mostrar, QLineEdit.ActionPosition.TrailingPosition)
        self.accion_cambiar_visibilidad.setShortcut(QKeySequence("Ctrl+M"))
        self.accion_cambiar_visibilidad.triggered.connect(self.cambiar_visibilidad)
        self.contraseña_visible = False

    def cambiar_visibilidad(self):
        if not self.contraseña_visible:
            self.setEchoMode(QLineEdit.EchoMode.Normal)
            self.contraseña_visible = True
            self.accion_cambiar_visibilidad.setIcon(self.ocultar)
        else:
            self.setEchoMode(QLineEdit.EchoMode.Password)
            self.contraseña_visible = False
            self.accion_cambiar_visibilidad.setIcon(self.mostrar)
