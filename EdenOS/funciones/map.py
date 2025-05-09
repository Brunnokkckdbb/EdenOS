import sys
import geocoder
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class MapaEnTiempoReal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mapa en Tiempo Real - Google Maps")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout(self)
        self.webview = QWebEngineView(self)
        self.layout.addWidget(self.webview)
        self.setLayout(self.layout)

        self.mostrar_mapa()

    def obtener_ubicacion(self):
        """Obtiene la ubicación actual."""
        g = geocoder.ip('me')
        if g.latlng:
            return g.latlng
        else:
            return None

    def obtener_url_google_maps(self, latitud, longitud, zoom=15):
        """Genera la URL de Google Maps para las coordenadas dadas."""
        return f"https://www.google.com/maps/@{latitud},{longitud},{zoom}z"

    def mostrar_mapa(self):
        """Carga el mapa de Google Maps en el QWebEngineView."""
        ubicacion = self.obtener_ubicacion()
        if ubicacion:
            latitud, longitud = ubicacion
            print(f"Latitud: {latitud}, Longitud: {longitud}")
            url_mapa = self.obtener_url_google_maps(latitud, longitud)
            self.webview.setUrl(QUrl(url_mapa))
        else:
            print("No se pudo obtener la ubicación actual.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MapaEnTiempoReal()
    window.show()
    sys.exit(app.exec_())