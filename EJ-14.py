"""

Crear un programa que solicite  una frase por teclado y muestre la
siguiente información:

-  La primera letra de cada palabra. Por ejemplo, si recibe Universal
Serial Bus debe devolver USB.

-  Dicha cadena con la primera letra de cada palabra en mayúsculas. Por
ejemplo, si recibe república argentina debe devolver República
Argentina.

-  Las palabras que comiencen con la letra A. Por ejemplo, si recibe
Antes de ayer debe devolver Antes ayer.

"""

def obtener_primera_letra(frase):
    palabras = frase.split()
    primera_letra_de_cada_palabra = ""

    for palabra in palabras:
        primera_letra_de_cada_palabra += palabra[0]

    return primera_letra_de_cada_palabra

def capitalizar_primera_letra(frase):

    palabras = frase.split()
    palabras_capitalizadas = []
    for palabra in palabras:
        palabras_capitalizadas.append(palabra.capitalize())

    return " ".join(palabras_capitalizadas)

def obtener_palabras_que_comienzan_con_a(frase):
    palabras = frase.split()
    palabras_que_comienzan_con_a = []

    for palabra in palabras:
        if palabra[0] == "A" or palabra[0] == "a":
            palabras_que_comienzan_con_a.append(palabra)

    return " ".join(palabras_que_comienzan_con_a)

def main():

    frase = input("\nIntroduce una frase: ")

    print("====================\n")
    print(f"--> [ {frase} ]")

    print("\nPROCESOS")
    print("========\n")

    primera_letra = obtener_primera_letra(frase)
    print(f"Primera letra de cada palabra: {primera_letra}")


    frase_con_primera_letra_mayuscula = capitalizar_primera_letra(frase)
    print(f"Frase con primera letra de cada palabra en mayúsculas: {frase_con_primera_letra_mayuscula}")

    palabras_que_comienzan_con_a = obtener_palabras_que_comienzan_con_a(frase)
    print(f"Palabras que comienzan con la letra A: {palabras_que_comienzan_con_a}")


main()


