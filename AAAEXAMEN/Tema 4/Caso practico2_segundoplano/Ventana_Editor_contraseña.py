from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QSystemTrayIcon, QMenu

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

        # Creamos un ícono para la bandeja del sistema
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("grifo.png"))

        # Creamos un menú para el ícono de la bandeja del sistema
        self.tray_menu = self.create_tray_menu()
        self.tray_icon.setContextMenu(self.tray_menu)

    def create_tray_menu(self):
#accion restaurar
        tray_menu = QMenu()
        restore_action = QAction("Restaurar", self)
        restore_action.triggered.connect(self.show)
        tray_menu.addAction(restore_action)
#accion salir
        quit_action = QAction("Salir", self)
        quit_action.triggered.connect(QApplication.instance().quit)
        tray_menu.addAction(quit_action)
        return tray_menu

    def closeEvent(self, event):
        event.ignore()  # Ignoramos el evento de cierre
        self.hide()  # Ocultamos la ventana
        self.tray_icon.show()  # Mostramos el ícono en la bandeja del sistema


if __name__ == "__main__":
    app = QApplication([])

    # Creamos una instancia de la ventana de configuración
    ventana_configuracion = VentanaConfiguracion()

    # Llamamos a cambiar_visibilidad() después de que la ventana sea mostrada
    ventana_configuracion.show()
    ventana_configuracion.editor_contrasena.cambiar_visibilidad()

    app.exec()
