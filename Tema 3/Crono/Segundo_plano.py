from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon, Qt, QAction
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu

from Cronometro.DI_U04_A02_01 import CronometroUI
from Cronometro.DI_U04_A03_01_0 import mostrar_aviso


@Slot()
def mostrar_ocultar():
    if cronometro.isHidden():
        cronometro.show()
    else:
        cronometro.hide()


if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon("circulo-de-flechas-en-sentido-horario.png"))  # asignamos un icono a la ventana
    app.setQuitOnLastWindowClosed(False)  # Para que no se cierre al cerrar la ultima ventana
    icon = QIcon(QIcon("circulo-de-flechas-en-sentido-horario.png"))
    # Agregamos la app al tray
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)
    tray.activated.connect(mostrar_ocultar)
    # Creamos un componente cronometro:
    cronometro = CronometroUI()
    # Cambiamos las propiedades del componente
    cronometro.setWindowTitle("Cronometro ")
    # Para que siempre sea visible
    cronometro.setWindowFlag(Qt.WindowStaysOnTopHint)
    # Crear un QAction y lo conectamos al slot para poder cerrar la app
    accion_salir = QAction("Salir", cronometro)
    accion_salir.triggered.connect(app.quit)
    # Creamos un menu y añadimos la accion:
    menu = QMenu()
    menu.addAction(accion_salir)
    # añadimos el menu al icono
    tray.setContextMenu(menu)
    # usamos la señal del componente
    cronometro.mensaje.connect(mostrar_aviso)

    cronometro.show()
    app.exec()
