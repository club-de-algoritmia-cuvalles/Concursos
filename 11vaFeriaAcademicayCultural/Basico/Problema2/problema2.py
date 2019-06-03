"""Problema 2 Solo numeros
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
    entrada = stdin.readline().strip()
    acumulador = 0 #  inicializamos un acumulador para almacenar el valor de los numeros
    for caracter in entrada:
        if caracter.isdigit():
            acumulador += int(caracter) # convertimos al caracter en int

    stdout.write('La suma es de: {}\n'.format(acumulador))
