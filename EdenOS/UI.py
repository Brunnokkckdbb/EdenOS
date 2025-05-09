import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtCore import Qt, QTimer, QTime, QSize
from PyQt5.QtGui import QFont, QCursor, QIcon, QPixmap

#importar los archivos de EDENOS/funciones/*
from funciones.map import MapaEnTiempoReal
from funciones.reverCam import *
from funciones.google import abrir_google




class PantallaCompletaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UI")
        self.initUI()
        self.pantalla_principal() # Mostrar la pantalla principal al inicio

        #dev
        #self.showFullScreen() # Mostrar la ventana en pantalla completa
        #self.setCursor(QCursor(Qt.BlankCursor)) # Ocultar el cursor
    def initUI(self):
        self.layout_principal = QGridLayout()
        self.setLayout(self.layout_principal)
        self.setGeometry(300, 300, 800, 600) # Establecer un tamaño inicial para la ventana

    def pantalla_principal(self):
        # Definir un tamaño para el botón (puedes ajustarlo)
        boton_ancho = 200
        boton_alto = 150

        # Limpiar cualquier widget anterior del layout
        for i in reversed(range(self.layout_principal.count())):
            widget = self.layout_principal.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)
        
        #RUTAS ICONOS 


        # iconos centro-izquierda-arriba
        ruta_botonSlep = r"funciones\assets\botonSlep.png"
        pixmap_botonSlep = QPixmap(ruta_botonSlep).scaled(QSize(boton_ancho, boton_alto), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icono_botonSlep = QIcon(pixmap_botonSlep)

        #iconos centro 
        ruta_botonCamara = r"funciones\assets\botonCamara.png"
        pixmap_botonCamara = QPixmap(ruta_botonCamara).scaled(QSize(boton_ancho, boton_alto), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icono_botonCamara = QIcon(pixmap_botonCamara)


        # iconos centro-derecha
        ruta_botonMap = r"funciones\assets\botonMap.png"
        pixmap_botonMap = QPixmap(ruta_botonMap).scaled(QSize(boton_ancho, boton_alto), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icono_botonMap = QIcon(pixmap_botonMap)

        # icono derecha abajo
        ruta_botonDerechaAbajo = r"funciones\assets\botonDerechaAbajo.png"
        pixmap_botonDerechaAbajo = QPixmap(ruta_botonDerechaAbajo).scaled(QSize(boton_ancho, boton_alto), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icono_botonDerechaAbajo = QIcon(pixmap_botonDerechaAbajo)


        # icono izquierda abajo
        ruta_botonIzquierdaAbajo = r"funciones\assets\botonIzquierdaAbajo.png"
        pixmap_botonIzquierdaAbajo = QPixmap(ruta_botonIzquierdaAbajo).scaled(QSize(boton_ancho, boton_alto), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icono_botonIzquierdaAbajo = QIcon(pixmap_botonIzquierdaAbajo)

        # icono centro
        ruta_botonCentro = r"funciones\assets\botoncentro.png"
        pixmap_botonCentro = QPixmap(ruta_botonCentro).scaled(QSize(boton_ancho, boton_alto), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icono_botonCentro = QIcon(pixmap_botonCentro)



        botones_info = [
            {'row': 1, 'col': 0, 'accion': self.revers_camera, 'icon': icono_botonCamara ,},
            {'row': 2, 'col': 0, 'accion': self.izquierda34, 'icon': icono_botonIzquierdaAbajo,},
            {'row': 0, 'col': 0, 'accion': self.IzquierdaArriba, 'icon': icono_botonSlep,},
            {'row': 1, 'col': 1, 'accion': self.CentroCentro, 'icon' : icono_botonCentro}, 
            {'row': 1, 'col': 2, 'accion': self.maps, 'icon': icono_botonMap},
            {'row': 2, 'col': 2, 'accion': self.derecha34, 'icon': icono_botonDerechaAbajo},
        ]

        # Crear y añadir los botones
        for info in botones_info:
            boton = QPushButton(info.get('text', ''), self) # El texto puede ser opcional si solo quieres el icono
            boton.setFont(QFont('Arial', 22))
            boton.clicked.connect(info['accion'])
            boton.setStyleSheet("border: none;") # ¡Esta línea elimina el borde!
            if 'icon' in info and info['icon']:
                boton.setIcon(info['icon'])
                boton.setIconSize(QSize(boton_ancho, boton_alto)) # Establecemos el tamaño del icono al del botón
                # boton.setText(info['text']) # Comentamos esta línea para que no se muestre el texto
                boton.setLayoutDirection(Qt.LeftToRight) # Opcional: dirección del texto respecto al icono (aunque no haya texto)

            if info.get('nombre') == 'Centro Centro':
                boton.setFixedSize(boton_ancho, boton_alto) # Establecemos el tamaño del botón

            self.layout_principal.addWidget(boton, info['row'], info['col'])

        # Crear el "botón-reloj"
        self.boton_reloj = QPushButton(self.obtener_hora(), self)
        self.boton_reloj.setFont(QFont('Arial', 28))
        self.boton_reloj.setStyleSheet("background-color: #333; color: white; border: none;") # También quitamos el borde del reloj
        self.boton_reloj.clicked.connect(self.accion_reloj)
        self.layout_principal.addWidget(self.boton_reloj, 0, 2)

        # Actualizar el texto del reloj cada segundo
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_reloj)
        self.timer.start(1000)


    def maps(self):
        # Limpiar cualquier widget anterior del layout
        for i in reversed(range(self.layout_principal.count())):
            widget = self.layout_principal.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        # Crear e instanciar el widget del mapa
        self.mapa_widget = MapaEnTiempoReal()
        self.layout_principal.addWidget(self.mapa_widget, 0, 0, 1, 3) # Añade el mapa al layout (ocupa toda la fila superior)

        # Crear y añadir el botón de volver (puedes ajustarlo según tu diseño)
        boton_volver = QPushButton("Volver", self)
        boton_volver.setFont(QFont('Arial', 22))
        boton_volver.clicked.connect(self.pantalla_principal)
        self.layout_principal.addWidget(boton_volver, 1, 1) # Centrado en la segunda fila
        
    def CentroCentro(self):
        # Limpiar cualquier widget anterior del layout
        for i in reversed(range(self.layout_principal.count())):
            widget = self.layout_principal.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

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
            widget = self.layout_principal.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

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
            widget = self.layout_principal.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

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
            widget = self.layout_principal.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

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
            widget = self.layout_principal.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

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
            widget = self.layout_principal.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

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