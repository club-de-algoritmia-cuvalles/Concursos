"""Problema 1 Contador Ascendente o Descendente
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
    #  incluyendo el salto de linea
    inferior = stdin.readline()
    superior = stdin.readline()
    paso = 1 # definimos una variable que indica el tipo de incremento que tendremos

    #  Convertir los valores a tipo entero, int ignora el salto de linea
    inferior, superior = int(inferior), int(superior)

    if inferior > superior:
        """Si el primer numero recibido es mayor al segundo, significa que la secuencia a imprimir
        es descendente, por lo que cambiamos nuestro paso a -1"""
        paso = -1

    """La clase range recibe 3 parametros (start, stop, step), start indica el numero de donde inicia
    nuestro rango, stop donde se detiene, excluyendo a este valor (por lo cual incrementamos o
    decrementamos en una unidad segun su caso), y step indica el incremento de la secuencia"""
    for numero in range(inferior, superior + paso, paso):
        """El metodo write de stdout no imprime un salto de linea
        implicitamente como la funcion print, por lo cual solo es
        necesario imprmir el nuemro seguido de un espacio en blanco
        para la salida"""
        stdout.write('{} '.format(numero))
    stdout.write('\n')
