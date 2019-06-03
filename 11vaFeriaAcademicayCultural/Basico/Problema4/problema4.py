"""Problema 4 Palabra Piramide Girada
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

    for i in range(1, len(palabra)+1): #  for para imprimir la parte superior de la piramide
        stdout.write('{}\n'.format(palabra[:i]))

    for i in range(len(palabra)-1, 0, -1): # for para imprimir la parte inferior de la piramide
        stdout.write('{}\n'.format(palabra[:i]))
