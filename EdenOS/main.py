#importo todo lo que este en la carpeta funciones 
from funciones import *  


numero = 10
cuadrado = calcular_cuadrado(numero)
print(f"El cuadrado de {numero} es: {cuadrado}")

texto = "Python"
invertido = invertir_texto(texto)
print(f"El texto invertido es: {invertido}")


# Carga de la UI 
if __name__ == '__main__':
    PantallaCompletaApp().run()