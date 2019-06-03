"""Problema 5 Buscando un caracter
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
Python 2.7"""

"""el uso del modulo sys para entrada/salida de datos es altamente
recomendado en programacion competitiva (ojo: no todas las competencias
permiten su uso), pero puede usar los metodos propios definidos en
python (raw_input y print)"""

from sys import stdin, stdout

if __name__ == '__main__':
    #  el metodo readline de stdin lee la siguiente linea de la entrada
    #  incluyendo el salto de linea, para eliminarlo usamos el metodo strip (sin parametros)
    #  de la clase str para eliminar los caracteres no deseados (espacios y saltos de linea)
    palabra = stdin.readline().strip()
    caracter_buscado = stdin.readline().strip()
    indices = [] # declaramos una lista vacia para almacenar los indices

    # utilizamos enumerate para devolver el indice y elemento iterado
    for indice, letra in enumerate(palabra):
        if letra == caracter_buscado:
            indices.append(str(indice))

    """"Para imprimir los indices separados por espacios, usamos el metodo join de la clase str
    el cual nos devuelve una cadena separada por la cadena de donde se invoca el metodo"""
    stdout.write('Ese caracter se encontro en las posiciones: {}\n'.format(', '.join(indices)))
    stdout.write('Se encontraron {} caracteres con la letra {}\n'.format(len(indices), caracter_buscado))
