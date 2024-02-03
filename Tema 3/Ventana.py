import json

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QApplication, QPushButton
import Si
import Datos_empresa

class SelectorEmpresa(QWidget):
    empresa_seleccionada = Signal(str)

    def __init__(self, empresas):
        super().__init__()
        self.empresas = empresas
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.buscar = QLineEdit()
        self.buscar.textChanged.connect(self.filtrar)
        layout.addWidget(self.buscar)

        self.widget_empresas = empresas(self.empresas, self)
        self.widget_empresas.empresa_seleccionada.connect(self.mostrar_empresa_seleccionada)
        layout.addWidget(self.widget_empresas)

    def mostrar_empresa_seleccionada(self, empresa_recibida):
        json_empresa_recibida = json.loads(empresa_recibida.replace('\n', '\\n'))
        for empresa in self.empresas:
            json_empresa = json.loads(empresa)
            if json_empresa_recibida['nombre'] == json_empresa['nombre']:
                self.empresa_seleccionada.emit(empresa_recibida)

    def filtrar(self, texto):
        for empresa in self.widget_empresas.empresas:
            if texto.lower() in empresa.nombre.lower():
                empresa.show()
            else:
                empresa.hide()


class Ventana(QWidget):
    def __init__(self):
        super(Ventana, self).__init__()
        self.layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(self.layout)
        self.widget_empresa = None
        self.setCentralWidget(widget)
        self.boton = QPushButton("Seleccionar empresa")
        self.layout.addWidget(self.boton)
        self.selector = SelectorEmpresa(datos_empresa.empresas)
        self.selector.empresa_seleccionada.connect(self.seleccionada)
        self.boton.clicked.connect(self.mostrar_selector)

    def mostrar_selector(self):
        self.selector.buscar.setFocus()
        self.selector.show()

    def seleccionada(self, empresa_recibida):
        json_empresa_recibida = json.loads(empresa_recibida.replace('\n', ''))
        if self.widget_empresa is None:
            self.widget_empresa = Si.Empresa(json_empresa_recibida, self)
            self.layout.addWidget(self.widget_empresa)
        else:
            self.widget_empresa.nombre = json_empresa_recibida['nombre']
            self.widget_empresa.direccion = json_empresa_recibida['direccion']
            self.widget_empresa.logo = json_empresa_recibida['logo']
        self.selector.buscar.clear()
        self.selector.hide()


if __name__ == "__main__":
    app = QApplication([])
    ventana = Ventana()
    ventana.show()
    app.exec()
