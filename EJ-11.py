"""

Realizar un programa que, dada una lista, devuelva una nueva lista cuyo contenido sea
igual a la  original pero invertida.

Por ejemplo: dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’, ‘papa’],
deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’].

"""

def invertir_lista(lista):
    lista_invertida = []
    for elemento in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[elemento])

    return lista_invertida

def main():

    lista = ['Di', 'buen', 'día', 'a', 'papa']
    lista_invertida = invertir_lista(lista)

    print(lista_invertida)

main()