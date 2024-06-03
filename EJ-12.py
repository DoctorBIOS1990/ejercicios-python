"""
Escribir un programa que dada una lista,
determine si está ordenada o no.

"""

def esta_ordenada_ascendente(lista):

    for i in range( 1, len(lista) ):
        if lista[ i ] < lista[ i - 1 ]:
            return False

    return True

def esta_ordenada_descendente(lista):

    for i in range( 1, len(lista) ):
        if lista[ i ] > lista[ i - 1 ]:
            return False

    return True

def main():

    lista1 = [1, 2, 3, 4, 5]
    lista2 = [5, 4, 3, 2, 1]

    print("\nASCENDENTE:")
    print("===========\n")

    print("La lista esta ordenada ascendente?", esta_ordenada_ascendente(lista1) )
    print("La lista esta ordenada ascendente?", esta_ordenada_ascendente(lista2) )

    print("\nDESCENDENTE:")
    print("===========\n")

    print("La lista esta ordenada ascendente?", esta_ordenada_descendente(lista1) )
    print("La lista esta ordenada descendente?", esta_ordenada_descendente(lista2) )

main()