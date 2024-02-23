from PySide6.QtCore import QTime, QTimer, Slot, QElapsedTimer, QSize, Qt, Signal  # Importa clases del módulo QtCore de PySide6
from PySide6.QtGui import QIcon  # Importa la clase QIcon del módulo QtGui de PySide6
from PySide6.QtWidgets import QLabel, QWidget, QPushButton, QVBoxLayout, QCheckBox, QTimeEdit, QHBoxLayout  # Importa clases de widgets del módulo QtWidgets de PySide6

class Cronometro():  # Define una clase Cronometro
    def __init__(self):  # Inicializa el objeto Cronometro
        self.__tiempo_transcurrido = QElapsedTimer()  # Inicializa un temporizador para el tiempo transcurrido
        self.__tiempo_pausa = QElapsedTimer()  # Inicializa un temporizador para el tiempo de pausa
        self.__acumulador = 0  # Inicializa un acumulador

    def iniciar(self):  # Método para iniciar el cronómetro
        self.__tiempo_transcurrido.restart()  # Reinicia el temporizador de tiempo transcurrido
        self.__acumulador = 0  # Reinicia el acumulador

    def obtenerTiempo(self):  # Método para obtener el tiempo transcurrido
        return QTime(0, 0).addMSecs(self.__tiempo_transcurrido.elapsed() - self.__acumulador)  # Retorna el tiempo transcurrido

    def pausar(self):  # Método para pausar el cronómetro
        self.__tiempo_pausa.restart()  # Reinicia el temporizador de pausa

    def continuar(self):  # Método para continuar el cronómetro después de pausarlo
        self.__acumulador = self.__acumulador + self.__tiempo_pausa.elapsed()  # Incrementa el acumulador con el tiempo de pausa

class CronometroUI(QWidget):  # Define una clase para la interfaz de usuario del cronómetro
    mensaje = Signal(str)  # Señal para enviar mensajes

    CRONOMETRO_RESET = 0  # Constante para estado de reinicio del cronómetro
    CRONOMETRO_INICIADO = 1  # Constante para estado de inicio del cronómetro
    CRONOMETRO_PAUSADO = 2  # Constante para estado de pausa del cronómetro
    CRONOMETRO_PARADO = 3  # Constante para estado de parada del cronómetro

    LISTA_ICONOS = {  # Diccionario para mapear nombres de iconos a rutas de archivo
        'play': ':/icons/play.png',
        'pause': ':/icons/pause.png',
        'stop': ':/icons/stop.png',
        'resume': ':/icons/resume.png',
        'restart': ':/icons/restart.png'
    }

    def __init__(self, parent=None):  # Inicializa la interfaz de usuario del cronómetro
        super().__init__(parent)  # Llama al constructor de la clase padre
        layout = QVBoxLayout()  # Crea un diseño vertical para la interfaz

        self.setLayout(layout)  # Establece el diseño de la ventana principal
        self.__estado = self.CRONOMETRO_RESET  # Inicializa el estado del cronómetro

        self.__cronometro = Cronometro()  # Crea una instancia de la clase Cronometro
        self.__tiempo = QTimer(self)  # Crea un temporizador para actualizar la GUI
        self.__tiempo_aviso = QTime(0, 0, 0, 0)  # Inicializa el tiempo para el aviso

        self.etiqueta = QLabel(QTime(0, 0).toString("hh:mm:ss"), self)  # Crea una etiqueta para mostrar el tiempo
        self.etiqueta.setMinimumHeight(50)  # Establece la altura mínima de la etiqueta
        self.etiqueta.setAlignment(Qt.AlignCenter)  # Alinea el texto al centro
        self.etiqueta.setStyleSheet(  # Establece el estilo de la etiqueta
            "background-color: white;"
            "border: 2px solid black;"
            "font-size: 25px"
        )

        self.boton_inicio = QPushButton(QIcon(self.LISTA_ICONOS['play']), "", self)  # Crea un botón de inicio
        self.boton_inicio.setIconSize(QSize(50, 50))  # Establece el tamaño del icono del botón
        self.boton_pausa = QPushButton(QIcon(self.LISTA_ICONOS['pause']), "", self)  # Crea un botón de pausa
        self.boton_pausa.setIconSize(QSize(50, 50))  # Establece el tamaño del icono del botón
        self.boton_pausa.setDisabled(True)  # Deshabilita el botón de pausa inicialmente

        self.aviso = QCheckBox("Avisar cuando llegue a ...", self)  # Crea una casilla de verificación para el aviso
        self.editor_tiempo_aviso = QTimeEdit(QTime(0, 0), self)  # Crea un editor de tiempo para el aviso
        self.editor_tiempo_aviso.setDisplayFormat("hh:mm:ss")  # Establece el formato de visualización

        layout_horizontal = QHBoxLayout()  # Crea un diseño horizontal para los controles de aviso
        layout_horizontal.addWidget(self.aviso)  # Agrega la casilla de verificación al diseño
        layout_horizontal.addWidget(self.editor_tiempo_aviso)  # Agrega el editor de tiempo al diseño

        layout.addLayout(layout_horizontal)  # Agrega el diseño horizontal al diseño vertical principal
        layout.addWidget(self.etiqueta)  # Agrega la etiqueta al diseño principal
        layout.addWidget(self.boton_inicio)  # Agrega el botón de inicio al diseño principal
        layout.addWidget(self.boton_pausa)  # Agrega el botón de pausa al diseño principal

        self.__tiempo.timeout.connect(self.actualizar_tiempo)  # Conecta la señal timeout del temporizador a la función de actualización del tiempo
        self.boton_inicio.clicked.connect(self.iniciar_parar)  # Conecta la señal clicked del botón de inicio a la función de inicio/parada
        self.boton_pausa.clicked.connect(self.pausar_continuar)  # Conecta la señal clicked del botón de pausa a la función de pausa/continuar
        self.editor_tiempo_aviso.timeChanged.connect(self.actualizar_tiempo_aviso)  # Conecta la señal timeChanged del editor de tiempo a la función de actualización del tiempo de aviso

    @Slot()  # Decorador para marcar un método como un slot
    def actualizar_tiempo(self):  # Método para actualizar el tiempo del cronómetro
        crono_actual = self.__cronometro.obtenerTiempo()  # Obtiene el tiempo actual del cronómetro
        self.etiqueta.setText(  # Actualiza el texto de la etiqueta con el tiempo actual
            crono_actual.toString("hh:mm:ss"))
        self.etiqueta.repaint()  # Repinta la etiqueta para actualizar el valor antes de lanzar el aviso
        if self.aviso.isChecked():  # Verifica si la casilla de verificación de aviso está marcada
            if -200 < self.__tiempo_aviso.msecsTo(crono_actual) < 200:  # Comprueba si el tiempo de aviso se ha alcanzado
                self.mensaje.emit("Tiempo límite alcanzado")  # Emite la señal de mensaje con el texto "Tiempo límite alcanzado"

    @Slot()  # Decorador para marcar un método como un slot
    def iniciar_parar(self):  # Método para iniciar o detener el cronómetro
        if self.__estado == self.CRONOMETRO_RESET:  # Verifica si el cronómetro está en estado de reinicio
            self.__cronometro.iniciar()  # Inicia el cronómetro
            self.__tiempo.start(1000)  # Inicia el temporizador para actualizar la GUI cada segundo
            self.__estado = self.CRONOMETRO_INICIADO  # Cambia el estado del cronómetro a iniciado
            self.boton_pausa.setDisabled(False)  # Habilita el botón de pausa
            self.boton_inicio.setIcon(QIcon(self.LISTA_ICONOS['stop']))  # Cambia el icono del botón de inicio a "stop"
        elif self.__estado == self.CRONOMETRO_PARADO:  # Verifica si el cronómetro está en estado de parada
            self.__estado = self.CRONOMETRO_RESET  # Cambia el estado del cronómetro a reinicio
            self.etiqueta.setText(  # Reinicia el texto de la etiqueta
                QTime(0, 0).toString("hh:mm:ss"))
            self.boton_inicio.setIcon(QIcon(self.LISTA_ICONOS['play']))  # Cambia el icono del botón de inicio a "play"
        else:  # Si el cronómetro está en estado iniciado
            self.__tiempo.stop()  # Detiene el temporizador para actualizar la GUI
            self.__estado = self.CRONOMETRO_PARADO  # Cambia el estado del cronómetro a parado
            self.boton_inicio.setIcon(QIcon(self.LISTA_ICONOS['restart']))  # Cambia el icono del botón de inicio a "restart"
            self.boton_pausa.setDisabled(True)  # Deshabilita el botón de pausa

    @Slot()  # Decorador para marcar un método como un slot
    def pausar_continuar(self):  # Método para pausar o continuar el cronómetro
        if self.__estado == self.CRONOMETRO_INICIADO:  # Si el cronómetro está en estado iniciado
            self.__cronometro.pausar()  # Pausa el cronómetro
            self.__tiempo.stop()  # Detiene el temporizador para actualizar la GUI

            self.__estado = self.CRONOMETRO_PAUSADO  # Cambia el estado del cronómetro a pausado
            self.boton_pausa.setIcon(QIcon(self.LISTA_ICONOS['resume']))  # Cambia el icono del botón de pausa a "resume"
            self.boton_inicio.setDisabled(True)  # Deshabilita el botón de inicio
        else:  # Si el cronómetro está en estado pausado
            self.__cronometro.continuar()  # Continúa el cronómetro después de la pausa
            self.__tiempo.start()  # Inicia el temporizador para actualizar la GUI

            self.__estado = self.CRONOMETRO_INICIADO  # Cambia el estado del cronómetro a iniciado
            self.boton_pausa.setIcon(QIcon(self.LISTA_ICONOS['pause']))  # Cambia el icono del botón de pausa a "pause"
            self.boton_inicio.setDisabled(False)  # Habilita el botón de inicio

    @Slot()  # Decorador para marcar un método como un slot
    def actualizar_tiempo_aviso(self):  # Método para actualizar el tiempo de aviso
        self.__tiempo_aviso = self.editor_tiempo_aviso.time()  # Obtiene el tiempo del editor de tiempo
