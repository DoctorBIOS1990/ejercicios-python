"""

Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a
cuantas horas y  minutos  corresponde.
Por  ejemplo:  1000  minutos son  16 horas  y  40 minutos.

"""


def determinar_tiempo(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return horas, minutos_restantes # Una tupla con el número de horas y minutos correspondientes.



def main():

    try:
        minutos = int( input("Inserte el tiempo en minutos:") )

        print("\nRESULTADO: ")
        print("===========\n")

        horas, minutos_restantes = determinar_tiempo(minutos)
        print(f"{minutos} minutos son {horas} horas y {minutos_restantes} minutos")

    except ValueError:
            print("Vuelva a escribir algo.")

main()


