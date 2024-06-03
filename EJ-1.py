"""

 Escribir un programa que pregunte al usuario su nombre,
 y luego lo salude.

"""
def main():
    try:
        nombre = input("Digite su nombre, por favor:")
        print("Hola " + nombre + " mucho gusto.")

    except ValueError:
            print("Vuelva a introducir los datos.")

main()

