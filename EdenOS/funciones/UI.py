import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QFont

class PantallaCompletaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pantalla Completa App")
        # self.showFullScreen() # Descomentar para pantalla completa
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        botones_info = [
            {'text': 'Izquierda Centro', 'row': 1, 'col': 0},
            {'text': 'Izquierda 3/4',    'row': 2, 'col': 0},
            {'text': 'Izquierda arriba', 'row': 0, 'col': 0},
            {'text': 'Centro Centro',    'row': 1, 'col': 1},
            {'text': 'Derecha Centro',   'row': 1, 'col': 2},
            {'text': 'Derecha 3/4',      'row': 2, 'col': 2},
        ]

        # Crear y añadir los botones
        for info in botones_info:
            boton = QPushButton(info['text'], self)
            boton.setFont(QFont('Arial', 22))
            boton.clicked.connect(self.accion_boton)
            grid.addWidget(boton, info['row'], info['col'])

        # Crear el "botón-reloj"
        self.boton_reloj = QPushButton(self.obtener_hora(), self)
        self.boton_reloj.setFont(QFont('Arial', 28))
        self.boton_reloj.setStyleSheet("background-color: #333; color: white;") # Un gris oscuro
        self.boton_reloj.clicked.connect(self.accion_reloj)
        grid.addWidget(self.boton_reloj, 0, 2)

        # Actualizar el texto del reloj cada segundo
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_reloj)
        self.timer.start(1000)

        self.setGeometry(300, 300, 800, 600) # Establecer un tamaño inicial para la ventana

    def obtener_hora(self):
        return QTime.currentTime().toString('hh:mm:ss')

    def actualizar_reloj(self):
        self.boton_reloj.setText(self.obtener_hora())

    def accion_boton(self):
        boton = self.sender()
        print(f'¡{boton.text()} presionado!')

    def accion_reloj(self):
        print("¡Reloj presionado! Puedes hacer algo aquí si quieres.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PantallaCompletaApp()
    ex.show()
    sys.exit(app.exec_())