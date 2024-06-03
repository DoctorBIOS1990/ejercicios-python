"""

Escribe un programa que lea una cadena y devuelva un diccionario con la
cantidad de apariciones de  cada palabra en la cadena.

Por ejemplo, si recibe
“Qué lindo día que hace hoy”

debe devolver: ‘que’: 2, ‘lindo’: 1, ‘día’: 1, ‘hace’: 1, ‘hoy’: 1

"""

def contar_palabras(cadena):
    palabras = cadena.split()
    cuenta_palabras = {}

    for palabra in palabras:
        if palabra not in cuenta_palabras:
            cuenta_palabras[ palabra ] = 0
        cuenta_palabras[ palabra ] += 1

    return cuenta_palabras

def main():

    #frase = "Qué lindo día que hace hoy"

    try:
        frase = input("\nIntroduce una frase: \n")
        cuenta_palabras = contar_palabras(frase)

        print("\nRESULTADO")
        print("=========")
        print("\n", cuenta_palabras)

    except ValueError:
        print("Vuelva a introducir los datos.")

main()
