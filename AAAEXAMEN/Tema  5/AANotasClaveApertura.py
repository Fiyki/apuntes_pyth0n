#Abrir html en local:
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices
from PySide6.QtWebEngineWidgets import QWebEngineView
def abrir_local(self):
    ruta_absoluta = "informe2.html"  # Ruta absoluta del archivo HTML
    view = QWebEngineView()  # Crea un widget QWebEngineView para mostrar contenido web
    view.setHtml(open(ruta_absoluta).read())  # Establece la URL del QWebEngineView como el archivo HTML

#Abrir en navegador:
def abrir_informe(self):  # Método para abrir el informe
    ruta_absoluta = "informe2.html"  # Ruta absoluta del archivo HTML
    QDesktopServices.openUrl(QUrl.fromLocalFile(ruta_absoluta))  # Abre la URL local en el navegador predeterminado