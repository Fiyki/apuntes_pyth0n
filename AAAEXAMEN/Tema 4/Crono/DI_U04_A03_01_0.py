from Cronometro import CronometroUI
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import Slot


@Slot()
def mostrar_aviso(mensaje):
    QMessageBox.information(cronometro, "Cronómetro PySide6", mensaje)

if __name__ == "__main__":
   
    app = QApplication([])
    
    # Asignamos un icono a la ventana
    app.setWindowIcon(QIcon(":/icons/cronometro.png"))
    
    # Creamos un componente cronómetro
    cronometro = CronometroUI()

    # Cambiamos propiedades del componente
    cronometro.setWindowTitle("Cronómetro PySide6")
    
    # Utilizamos la señal del componente
    cronometro.mensaje.connect(mostrar_aviso)
    
    cronometro.show()
        
    app.exec()