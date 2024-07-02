"""
En este ejemplo crearemos un nuevo tipo llamado  NumeroComplejo.
Este tipo tiene un atributo  x para la coordenada en x e y para la
coordenada en y. Representa un número complejo de la forma (x, y).

a)  Definir para la clase  NumeroComplejo  un método que permita imprimir
    una instancia de la clase.  Recordar que, al intentar imprimir un tipo
    definido por nosotros, se imprime la dirección de memoria.

b)  Definir una función que compara dos números complejos,
    - Tener en cuenta que, si dos objetos distintos tienen sus atributos
    iguales, no se consideran iguales.

c)  Definir un método que sume dos números complejos y retorne  el
    resultado en un objeto de tipo NumeroComplejo.

"""

class NumeroComplejo:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def look_Object(self):
        print("\n:) Hi, my coordinate is (x = ", self.x , "& y = ", self.y,")")


def check_complex_numbers(numero_complejo1, numero_complejo2):

    if ((numero_complejo1.x != numero_complejo2.x) and
        (numero_complejo1.y != numero_complejo2.y)):
         print("    * The numbers are different.")


def addition_complex_numbers(numero_complejo1, numero_complejo2):

    result = NumeroComplejo( numero_complejo1.x + numero_complejo2.x, numero_complejo1.y + numero_complejo2.y)
    return result

def main():

    # Create complex numbers
    my_number = NumeroComplejo(20, 40)
    my_number2= NumeroComplejo(50, 100)

    # Looking Data
    my_number.look_Object()

    print("\n-->PROCESSING, PLEASE WAIT....")
    # Check two complex numbers
    check_complex_numbers(my_number, my_number2)

    # Addition complex numbers
    print("    * The result addition is: (x = "
    ,addition_complex_numbers(my_number, my_number2).x,"and y = ",
    addition_complex_numbers(my_number, my_number2).y,")")







main()


