"""

Escribe un programa que permita leer por teclado números y guardarlo en una lista, el
proceso finaliza cuando se inserte un número negativo. Muestre el máximo de los
números guardados en la lista, y los números pares.

"""
def main():

    numeros = []

    while True:
        numero = float(input("Introduce un número (Un número negativo para finalizar): "))

        if numero < 0:
            break
        numeros.append(numero)

    print("\nEl máximo de los números introducidos es: -->", max(numeros) )

    print("\nLos números pares introducidos son:")
    print("===================================")

    for numero in numeros:
        if numero % 2 == 0:
            print("-->", numero)

main()