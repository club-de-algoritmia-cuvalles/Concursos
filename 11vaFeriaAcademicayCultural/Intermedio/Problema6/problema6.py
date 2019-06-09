"""Problema 6 Mateo Towers
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
Python 2.7"""
from collections import OrderedDict
from sys import stdin

if __name__ == '__main__':
    t = stdin.readline() # numero de cubos a recibir
    bloques = stdin.readline().strip() # cubos recibidos

    """sub-clase de diccionario (tabla hash) que conserva el orden
    de inserccion de las llaves (valido para las versiones menores a 3.6)
    Para python 3.6+ los diccionarios conservan el orden de inserccion
    """
    torres = OrderedDict()

    for bloque in bloques:
        letra = bloque.upper() # convertir en mayuscula el cubo
        t_letra = bloque.isupper() # comprobar si la letra es mayuscula(True) o minuscula(False)
        try:
            if t_letra: #comprobar si la letra es mayuscula, para
                torres[letra] += 1
            else:
                torres[letra] -= 1 #disminuir la torre
                if not torres[letra]: # si la torre no tiene bloques, se elimina
                    torres.pop(letra)
        except KeyError: # llave no existe
            if t_letra:
                torres[letra] = 1 #inicializar la torre con 1

    if not torres:
        print('0')
    else:
        for torre, cant in torres.items():
            print('{}{}'.format(torre, cant)) #imprimir las torres
