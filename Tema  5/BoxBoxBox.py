from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QComboBox


class VentanaInformes(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Configuración del diseño vertical para la ventana
        self.layout_vertical = QVBoxLayout()
        self.setLayout(self.layout_vertical)

        # Creación del ComboBox para seleccionar informes
        self.combobox_informes = QComboBox()
        self.combobox_informes.addItem("Informe 1")
        self.combobox_informes.addItem("Informe 2")
        self.combobox_informes.addItem("Informe 3")
        # Conexión del evento de cambio de selección con el método abrir_informe
        self.combobox_informes.currentIndexChanged.connect(self.abrir_informe)
        self.layout_vertical.addWidget(self.combobox_informes)

        # Creación de la vista del navegador web para mostrar los informes
        self.view = QWebEngineView()
        self.layout_vertical.addWidget(self.view)

        # Establecimiento del tamaño inicial de la ventana
        self.resize(600, 800)

        # Llamada al método abrir_informe para cargar el informe al iniciar la ventana
        self.abrir_informe()

    # Método para abrir el informe seleccionado
    def abrir_informe(self):
        # Obtención del texto seleccionado en el ComboBox
        informe_seleccionado = self.combobox_informes.currentText()
        # Definición de las rutas de los informes según la selección
        if informe_seleccionado == "Informe 1":
            ruta = "Informe.html"
        elif informe_seleccionado == "Informe 2":
            ruta = "InformeDeVentas.html"
        else:
            ruta = "Informe1.html"

        # Lectura del contenido HTML del informe seleccionado y carga en la vista del navegador web
        self.view.setHtml(open(ruta).read())


# Entrada principal del programa
if __name__ == "__main__":
    # Creación de la aplicación Qt
    app = QApplication([])
    # Creación de la ventana de informes y visualización
    ventana_informes = VentanaInformes()
    ventana_informes.show()
    # Ejecución del bucle de eventos de la aplicación
    app.exec()
