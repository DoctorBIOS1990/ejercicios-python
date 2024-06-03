"""

 Escribir  un  programa  que dados  dos  números,
 realice y muestre  la  suma, resta,  división
 y multiplicación de ambos.

"""

def suma(Numero1, Numero2):
    return str( Numero1 + Numero2)

def resta(Numero1, Numero2):
    return str( Numero1 - Numero2)

def multiplicacion(Numero1, Numero2):
    return str( Numero1 * Numero2)

def division(Numero1, Numero2):
    return str( Numero1 / Numero2)


def main():

    try:
        numero1 = float(input("Inserte PRIMER numero:"))
        numero2 = float(input("Inserte SEGUNDO numero:"))

        print("\nRESULTADOS: ")
        print("===========")

        print("La Suma es: " + suma(numero1, numero2) )
        print("La Resta es: " + resta(numero1, numero2) )
        print("La Multiplicacion es: " + multiplicacion(numero1, numero2) )
        print("La Division es: " + division(numero1, numero2) )


    except ValueError:
            print("Vuelva a introducir los datos.")

main()
