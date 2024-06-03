"""

 Escribir  un  programa  que permita calcular  el  perímetro
 y  área  de  un  rectángulo. Primero deberá solicitar los
 valores de la base y altura al usuario.

"""

def calcular_perimetro(base, altura):
    return str( (base * 2) + (altura * 2) )

def calcular_area(base, altura):
    return str( base * altura )


def main():

    try:
        base = float(input("Inserte valor de la Base:"))
        altura = float(input("Inserte valor de la Altura:"))

        print("\nRESULTADOS: ")
        print("===========")

        print("El perimetro es: " + calcular_perimetro(base, altura) )
        print("El area es: " +  calcular_area(base, altura) )

    except ValueError:
            print("Vuelva a introducir los datos.")

main()


