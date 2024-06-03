"""

 Escribir un programa que le pida una palabra al usuario, para luego imprimirla 1000
 veces, con espacios intermedios.

"""

def main():

    try:
        palabra = input("Escriba algo:")

        print("\nREPETICIONES: ")
        print("===========\n")

        print( (palabra + " ") * 1000 )


    except ValueError:
            print("Vuelva a escribir algo.")

main()
