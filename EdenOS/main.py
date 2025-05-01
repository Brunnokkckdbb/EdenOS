from funciones import *
import sys
from PyQt5.QtWidgets import QApplication

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