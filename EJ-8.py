"""

Crea una aplicación que permita adivinar un número.
En primer lugar, la aplicación solicita un número entero por teclado.

A continuación, va pidiendo números y va expondiendo si el número
a adivinar es mayor o menor que el introducido.

El programa termina cuando se acierta el número.

"""

def main():

    try:
        numero_introducido = float( input("Introduce un número entre 1 y 10:") )
        numero_adivinar = 0

        print("\nRESULTADO: ")
        print("===========\n")

        while numero_introducido != numero_adivinar:

            if numero_introducido < numero_adivinar:
                print("El número a adivinar es mayor\n")
            else:
                print("El número a adivinar es menor")

            numero_adivinar = float( input("Introduce un número entre 1 y 10: ") )


        print("\nHas acertado el número!!!")

    except ValueError:
            print("Vuelva a escribir los numeros.")

main()







