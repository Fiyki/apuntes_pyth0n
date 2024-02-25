import os  # Importa el módulo os para interactuar con el sistema operativo

from PySide6.QtGui import QIcon, QKeySequence  # Importa clases necesarias de PySide6
from PySide6.QtWidgets import QLineEdit


class EditorContraseña(QLineEdit):  # Define una clase personalizada que hereda de QLineEdit
    def __init__(self, parent=None):
        super().__init__(parent)  # Llama al constructor de la clase base

        # Obtiene la ruta del directorio actual del script
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Rutas relativas a los iconos
        mostrar_icon_path = os.path.join(current_directory, "verde.png")
        ocultar_icon_path = os.path.join(current_directory, "rojo.png")

        # Verificar si los archivos de íconos existen
        if os.path.exists(mostrar_icon_path) and os.path.exists(ocultar_icon_path):
            self.mostrar = QIcon(mostrar_icon_path)  # Crea un objeto QIcon para el ícono mostrar
            self.ocultar = QIcon(ocultar_icon_path)  # Crea un objeto QIcon para el ícono ocultar
        else:
            raise FileNotFoundError("No se pueden encontrar los archivos de íconos.")

        # Configura el QLineEdit para ocultar el texto (modo contraseña) y muestra un texto de marcador de posición
        self.setEchoMode(QLineEdit.EchoMode.Password)
        self.setPlaceholderText("Introduce tu contraseña")

        # Agrega un botón al QLineEdit para cambiar la visibilidad de la contraseña
        self.accion_cambiar_visibilidad = self.addAction(self.mostrar, QLineEdit.ActionPosition.TrailingPosition)
        self.accion_cambiar_visibilidad.setShortcut(QKeySequence("Ctrl+M"))  # Establece un atajo de teclado
        self.accion_cambiar_visibilidad.triggered.connect(
            self.cambiar_visibilidad)  # Conecta la acción del botón a una función
        self.contraseña_visible = False  # Inicializa una bandera para rastrear la visibilidad de la contraseña

    # Función para cambiar la visibilidad de la contraseña
    def cambiar_visibilidad(self):
        if not self.contraseña_visible:
            self.setEchoMode(QLineEdit.EchoMode.Normal)
            self.contraseña_visible = True
            self.accion_cambiar_visibilidad.setIcon(self.ocultar)
        else:
            self.setEchoMode(QLineEdit.EchoMode.Password)
            self.contraseña_visible = False
            self.accion_cambiar_visibilidad.setIcon(self.mostrar)
