"""

Elabore un programa que muestre la tabla de multiplicar
de los números 1,2,3,4 y 5.

"""

def construir_tabla(numero):

    for i in range(0,9):
        print ( str(numero) + " * " + str(i + 1) + " = " + str(numero * (i + 1) ) + "\n")

def main():

        print("\nTABLA DE 1: ")
        print("===========\n")
        construir_tabla(1)

        print("\nTABLA DE 2: ")
        print("===========\n")
        construir_tabla(2)

        print("\nTABLA DE 3: ")
        print("===========\n")
        construir_tabla(3)

        print("\nTABLA DE 4: ")
        print("===========\n")
        construir_tabla(4)

        print("\nTABLA DE 5: ")
        print("===========\n")
        construir_tabla(5)

main()
