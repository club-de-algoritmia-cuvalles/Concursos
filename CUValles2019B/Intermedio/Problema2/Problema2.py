"""
Problema 2: The search for toys
Autor de la solucion: Luis Arturo DLG.
Python 3.x

Descripcion del problema:Recibremos 2 conjuntos de cadenas y deberemos de buscar
a todos los elementos del primer conjunto que no se encuentren en el segundo

Ejemplo 1:
Entrada:
5
ball car aeroplane marble cubes
3
ball cubes car

Salida:
aeroplane marble

Ejemplo 2:
Entrada:
6
car cowboy horse spinner cow tractor
4
car cowboy cow tractor

Salida:
aeroplane marble

Explicacion:
Tendremos que realizar una busqueda de los elementos del primer conjunto en el
segundo conjunto, otra manera de visualizarlo es a traves de conjuntos, si nos
damos cuenta, en los conjuntos no se repiten elementos, por lo que empleando
una estructura que funcione como un conjunto matematico, para realizar
la operacion de diferencia

Ejemplo:
conjunto 1 = {ball, car, aeroplane, marble, cubes}
conjunto 2 = {ball, cubes, car}

Si observamos los elementos 'ball', 'cubes'  y 'car' existen en ambos conjuntos,
por lo que los elementos restantes ('aeroplane' y 'marble') son la diferencia
entre ambos conjuntos
"""

def busqueda(elemento, conjunto):
    """
    Funcion que devuelve si un elemento se encuentra o no en el conjunto
    parametros:
    > elemento: str
    > conjunto: List[str]
    retorno:
    bool que indica si elemento se encuentra o no en el conjunto
    """
    for c in conjunto:

        if c == elemento: # si el elemento es igual
            return True

    return False # si el elemento no se encuentra


def diferencia(conjunto1, conjunto2):
    """
    Funcion que devuelve los elementos del conjunto 1 que no se encuentran en
    el conjunto 2.
    parametros:
    > conjunto1 = List[str]
    > conjunto2 = List[str]
    retorno:
    list con los elementos del conjunto1 que no estan en conjunto2
    """
    conjunto3 = [] # lista para almacenar la diferencia entre conjuntos

    for elemento in conjunto1:

        if busqueda(elemento, conjunto2) == False: # si el elemento no se encuentra
            conjunto3.append(elemento) # agregamos el elemento al conjunto

    return conjunto3


if __name__ == '__main__': # main del programa
    """
    Nota: en python no es necesario saber cuantos elementos debemos recibir
    para formar listas, pero se deben de leer las entradas si se ha especificado
    en el problema.
    """
    #modo manual
    n = int(input()) # numero de productos en la dispensadora
    """
    Para obtener una lista de los elementos separados por espacio, podemos usar
    metodo split para generar una lista con el espacio como separador por
    default
    """
    conjunto1 = input().split() # lista de Productos
    k = int(input()) # numero de productos a buscar
    conjunto2 = input().split()
    conjunto3 = diferencia(conjunto1, conjunto2)

    """
    Modo Rapido
    Python tiene una clase standar llamada set, el cual nos
    permite realizar las operacions que se pueden hacer con los conjuntos
    matemaiticos
    conjunto1 = set(input().split())
    conjunto2 = set(input().split())
    conjunto3 = conjunto1 - conjunto2
    """
    print(' '.join(conjunto3))
