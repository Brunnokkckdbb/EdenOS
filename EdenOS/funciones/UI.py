import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QFont

class PantallaCompletaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UI")
        self.initUI()
        self.pantalla_principal() # Mostrar la pantalla principal al inicio
        #self.showFullScreen() # Mostrar la ventana en pantalla completa
    def initUI(self):
        self.layout_principal = QGridLayout()
        self.setLayout(self.layout_principal)

        self.setGeometry(300, 300, 800, 600) # Establecer un tamaño inicial para la ventana

    def pantalla_principal(self):
        # Limpiar cualquier widget anterior del layout
        for i in reversed(range(self.layout_principal.count())):
            self.layout_principal.itemAt(i).widget().setParent(None)

        botones_info = [
            {'text': 'Izquierda Centro', 'row': 1, 'col': 0, 'accion': self.revers_camera},
            {'text': 'Izquierda 3/4',     'row': 2, 'col': 0, 'accion': self.izquierda34},
            {'text': 'Izquierda arriba', 'row': 0, 'col': 0, 'accion': self.IzquierdaArriba},
            {'text': 'Centro Centro',     'row': 1, 'col': 1, 'accion': self.CentroCentro},
            {'text': 'Derecha Centro',    'row': 1, 'col': 2, 'accion': self.maps},
            {'text': 'Derecha 3/4',       'row': 2, 'col': 2, 'accion': self.derecha34},
        ]

        # Crear y añadir los botones
        for info in botones_info:
            boton = QPushButton(info['text'], self)
            boton.setFont(QFont('Arial', 22))
            boton.clicked.connect(info['accion'])
            self.layout_principal.addWidget(boton, info['row'], info['col'])

        # Crear el "botón-reloj"
        self.boton_reloj = QPushButton(self.obtener_hora(), self)
        self.boton_reloj.setFont(QFont('Arial', 28))
        self.boton_reloj.setStyleSheet("background-color: #333; color: white;") # Un gris oscuro
        self.boton_reloj.clicked.connect(self.accion_reloj)
        self.layout_principal.addWidget(self.boton_reloj, 0, 2)

        # Actualizar el texto del reloj cada segundo
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_reloj)
        self.timer.start(1000)


    def maps(self):
        # Limpiar cualquier widget anterior del layout
        for i in reversed(range(self.layout_principal.count())):
            self.layout_principal.itemAt(i).widget().setParent(None)

        # Crear y añadir el contenido de la nueva pantalla
        etiqueta = QLabel("¡Esta es otra pantalla!", self)
        etiqueta.setFont(QFont('Arial', 36))
        self.layout_principal.addWidget(etiqueta, 0, 0, 1, 3) # Ocupa toda la fila superior

        boton_volver = QPushButton("Volver", self)
        boton_volver.setFont(QFont('Arial', 22))
        boton_volver.clicked.connect(self.pantalla_principal)
        self.layout_principal.addWidget(boton_volver, 1, 1) # Centrado en la segunda fila

    def CentroCentro(self):
        # Limpiar cualquier widget anterior del layout
        for i in reversed(range(self.layout_principal.count())):
            self.layout_principal.itemAt(i).widget().setParent(None)

        # Crear y añadir el contenido de la nueva pantalla
        etiqueta = QLabel("¡Esta es otra pantalla!", self)
        etiqueta.setFont(QFont('Arial', 36))
        self.layout_principal.addWidget(etiqueta, 0, 0, 1, 3) # Ocupa toda la fila superior

        boton_volver = QPushButton("Volver", self)
        boton_volver.setFont(QFont('Arial', 22))
        boton_volver.clicked.connect(self.pantalla_principal)
        self.layout_principal.addWidget(boton_volver, 1, 1) # Centrado en la segunda fila

    def IzquierdaArriba(self):
        # Limpiar cualquier widget anterior del layout
        for i in reversed(range(self.layout_principal.count())):
            self.layout_principal.itemAt(i).widget().setParent(None)

        # Crear y añadir el contenido de la nueva pantalla
        etiqueta = QLabel("¡Esta es otra pantalla!", self)
        etiqueta.setFont(QFont('Arial', 36))
        self.layout_principal.addWidget(etiqueta, 0, 0, 1, 3) # Ocupa toda la fila superior

        boton_volver = QPushButton("Volver", self)
        boton_volver.setFont(QFont('Arial', 22))
        boton_volver.clicked.connect(self.pantalla_principal)
        self.layout_principal.addWidget(boton_volver, 1, 1) # Centrado en la segunda fila

    def izquierda34(self):
        # Limpiar cualquier widget anterior del layout
        for i in reversed(range(self.layout_principal.count())):
            self.layout_principal.itemAt(i).widget().setParent(None)

        # Crear y añadir el contenido de la nueva pantalla
        etiqueta = QLabel("¡Esta es otra pantalla!", self)
        etiqueta.setFont(QFont('Arial', 36))
        self.layout_principal.addWidget(etiqueta, 0, 0, 1, 3) # Ocupa toda la fila superior

        boton_volver = QPushButton("Volver", self)
        boton_volver.setFont(QFont('Arial', 22))
        boton_volver.clicked.connect(self.pantalla_principal)
        self.layout_principal.addWidget(boton_volver, 1, 1) # Centrado en la segunda fila

    def derecha34(self):
        # Limpiar cualquier widget anterior del layout
        for i in reversed(range(self.layout_principal.count())):
            self.layout_principal.itemAt(i).widget().setParent(None)

        # Crear y añadir el contenido de la nueva pantalla
        etiqueta = QLabel("¡Esta es otra pantalla!", self)
        etiqueta.setFont(QFont('Arial', 36))
        self.layout_principal.addWidget(etiqueta, 0, 0, 1, 3) # Ocupa toda la fila superior

        boton_volver = QPushButton("Volver", self)
        boton_volver.setFont(QFont('Arial', 22))
        boton_volver.clicked.connect(self.pantalla_principal)
        self.layout_principal.addWidget(boton_volver, 1, 1) # Centrado en la segunda fila

    def revers_camera(self):
        # Limpiar cualquier widget anterior del layout
        for i in reversed(range(self.layout_principal.count())):
            self.layout_principal.itemAt(i).widget().setParent(None)

        # Crear y añadir el contenido de la nueva pantalla
        etiqueta = QLabel("¡Esta es otra pantalla!", self)
        etiqueta.setFont(QFont('Arial', 36))
        self.layout_principal.addWidget(etiqueta, 0, 0, 1, 3) # Ocupa toda la fila superior

        boton_volver = QPushButton("Volver", self)
        boton_volver.setFont(QFont('Arial', 22))
        boton_volver.clicked.connect(self.pantalla_principal)
        self.layout_principal.addWidget(boton_volver, 1, 1) # Centrado en la segunda fila

    def obtener_hora(self):
        return QTime.currentTime().toString('hh:mm:ss')

    def actualizar_reloj(self):
        self.boton_reloj.setText(self.obtener_hora())

    def accion_boton(self):
        boton = self.sender()
        print(f'¡{boton.text()} presionado!')

    def accion_reloj(self):
        # Limpiar cualquier widget anterior del layout
        for i in reversed(range(self.layout_principal.count())):
            self.layout_principal.itemAt(i).widget().setParent(None)

        # Crear y añadir el contenido de la nueva pantalla
        etiqueta = QLabel("¡Esta es otra pantalla!", self)
        etiqueta.setFont(QFont('Arial', 36))
        self.layout_principal.addWidget(etiqueta, 0, 0, 1, 3) # Ocupa toda la fila superior

        boton_volver = QPushButton("Volver", self)
        boton_volver.setFont(QFont('Arial', 22))
        boton_volver.clicked.connect(self.pantalla_principal)
        self.layout_principal.addWidget(boton_volver, 1, 1) # Centrado en la segunda fila


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PantallaCompletaApp()
    ex.show()
    sys.exit(app.exec_())