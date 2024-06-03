"""

 Calcular  el  perímetro y  área  de  un  círculo.
 Primero deberá solicitar  el valor  del  radio  al usuario.

"""
import math

def calcular_perimetro(radio):
    return str( 2 * math.pi * radio)

def calcular_area(radio):
    return str( math.pi * radio**2  )   #  PI * R2


def main():

    try:
        radio = float(input("Inserte valor de la Base:"))

        print("\nRESULTADOS: ")
        print("===========")

        print("El perimetro del circulo es: " + calcular_perimetro(radio) )
        print("El area del circulo es: " +  calcular_area(radio) )

    except ValueError:
            print("Vuelva a introducir los datos.")

main()

