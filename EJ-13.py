"""

Escribe un programa que diga si un número introducido por teclado es o
no primo. Un número primo es aquel que sólo es divisible entre él mismo y
la unidad.

"""

def es_primo(numero):

    if numero <= 1:
        return False

    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            return False

    return True

def main():

    try:
        numero = int(input("Introduce un número: "))

        if es_primo(numero):
            print(f"{numero} es un número primo")
        else:
            print(f"{numero} no es un número primo")

    except ValueError:
        print("Vuelva a introducir los datos.")

main()

