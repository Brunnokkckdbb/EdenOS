import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

def abrir_google():
    app = QApplication(sys.argv)
    ventana = QWidget()
    vista_web = QWebEngineView()
    vista_web.load(QUrl("https://www.google.com"))
    vista_web.setWindowTitle("Google")
    layout = QVBoxLayout()
    layout.addWidget(vista_web)
    ventana.setLayout(layout)
    ventana.setGeometry(100, 100, 800, 600)  # (x, y, ancho, alto)
    ventana.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    abrir_google()