"""

Realiza un programa que solicite dos números ‘a’ y ‘b’ al usuario,
e indique si su suma es #positiva, negativa o cero.

"""


def evaluar(a,b):
    return a + b

def main():

    try:
        a = float( input("Escriba un numero:") )
        b = float( input("Escriba otro numero:") )

        print("\nRESULTADO: ")
        print("===========\n")

        if ( evaluar(a,b) ) > 0:
            print("La suma es positiva.")

        elif ( evaluar(a,b) ) < 0:
            print("La suma es negativa.")

        else:
            print("La suma es cero.")


    except ValueError:
            print("Vuelva a escribir algo.")

main()