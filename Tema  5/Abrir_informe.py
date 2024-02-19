from PySide6.QtCore import QUrl  # Importa la clase QUrl del módulo QtCore de PySide6
from PySide6.QtGui import QDesktopServices  # Importa la clase QDesktopServices del módulo QtGui de PySide6
from PySide6.QtWebEngineWidgets import QWebEngineView  # Importa la clase QWebEngineView del módulo QtWebEngineWidgets de PySide6
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton,QApplication  # Importa las clases QWidget, QVBoxLayout, QPushButton y QApplication del módulo QtWidgets de PySide6


class VentanaInformes(QWidget):  # Definición de una clase VentanaInformes que hereda de QWidget
    def __init__(self, parent=None):  # Método constructor de la clase
        super().__init__(parent)  # Llama al constructor de la clase base (QWidget)
        self.layout_vertical = QVBoxLayout(self)  # Crea un layout vertical y lo asigna al widget principal

        boton_abrir = QPushButton('Abrir informe')  # Crea un botón con el texto 'Abrir informe'
        boton_abrir.clicked.connect(
            self.abrir_informe)  # Conecta la señal clicked del botón con el método abrir_informe
        self.layout_vertical.addWidget(boton_abrir)  # Agrega el botón al layout vertical

        ruta_absoluta = "C:/GitHub/apuntes_pyth0n/apuntes_pyth0n/Tema  5/informe2.html"  # Ruta absoluta del archivo HTML
        view = QWebEngineView()  # Crea un widget QWebEngineView para mostrar contenido web
        view.setUrl(QUrl.fromLocalFile(ruta_absoluta))  # Establece la URL del QWebEngineView como el archivo HTML
        self.layout_vertical.addWidget(view)  # Agrega el QWebEngineView al layout vertical

        self.resize(600, 800)  # Establece el tamaño inicial de la ventana

    def abrir_informe(self):  # Método para abrir el informe
        ruta_absoluta = "C:/GitHub/apuntes_pyth0n/apuntes_pyth0n/Tema  5/informe2.html"  # Ruta absoluta del archivo HTML
        QDesktopServices.openUrl(QUrl.fromLocalFile(ruta_absoluta))  # Abre la URL local en el navegador predeterminado


if __name__ == '__main__':  # Si se ejecuta el script como programa principal
    app = QApplication([])  # Crea una instancia de QApplication
    main = VentanaInformes()  # Crea una instancia de la ventana principal
    main.show()  # Muestra la ventana
    app.exec()  # Ejecuta el bucle de eventos de la aplicación
