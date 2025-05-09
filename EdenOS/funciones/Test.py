import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

def abrir_tv():
    app = QApplication(sys.argv)
    ventana = QWidget()
    vista_web = QWebEngineView()
    vista_web.load(QUrl("https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwibsdDx-JGNAxW5s5UCHZnPDOMQFnoECA4QAQ&url=https%3A%2F%2Ftv.garden%2Far&usg=AOvVaw08b9rw55rCcF-E6dLRFu-j&opi=89978449"))
    vista_web.setWindowTitle("TV")
    layout = QVBoxLayout()
    layout.addWidget(vista_web)
    ventana.setLayout(layout)
    ventana.setGeometry(100, 100, 800, 600)  # (x, y, ancho, alto)
    ventana.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    abrir_tv()