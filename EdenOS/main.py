import sys
import os

# Obtiene la ruta absoluta del directorio donde se encuentra main.py (EDENOS)
ruta_edenos = os.path.abspath(os.path.dirname(__file__))

# Obtiene la ruta del directorio padre de EDENOS
ruta_padre = os.path.dirname(ruta_edenos)

# Añade el directorio padre al sys.path si no está ya
if ruta_padre not in sys.path:
    sys.path.append(ruta_padre)

from funciones import *
from PyQt5.QtWidgets import QApplication
from UI import PantallaCompletaApp  # Importa directamente UI aquí

numero = 10
cuadrado = calcular_cuadrado(numero)
print(f"El cuadrado de {numero} es: {cuadrado}")

texto = "Python"
invertido = invertir_texto(texto)
print(f"El texto invertido es: {invertido}")


# Carga de la UI
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PantallaCompletaApp()
    ex.show()
    sys.exit(app.exec_())