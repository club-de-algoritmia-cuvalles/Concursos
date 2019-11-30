"""
Problema 5: Combined cards
Autor de la solucion: Luis Arturo DLG.
Python 3.x

Descripcion del problema: Calcular las combinaciones posibles de un conjunto de
n cartas, terminamos hasta encontrar un 0.

Ejemplo:
Entrada:
3
5
0

Salida:
6
120

Explicacion: Para calcular las combinaciones posibles de n cartas, donde las
posiciones de estas afectan la combinacion, obtendremos que el resultado es
igual a el factorial del n. Ejemplo:
n = 3
1) 1,2,3
2) 1,3,2
3) 2,1,3
4) 2,3,1
5) 3,1,2
6) 3,2,1

3! = 6

Para calcular el factorial de n, debemos de usar la funcion recursiva:
n! = n * n-1 * n-2 * ... * 1
Ejemplo:
3! = 3 * 2 * 1 = 6
"""

def factorial(n):
    """
    Funcion para calcular el factorial de un numero n
    > n: int
    retorno:
    int con el valor del factorial de n
    """
    if n == 1: # si n es igual a 1
        return 1

    """
    Escribimos la funcion recursiva en base a la formula:
    n! = n * n-1 * n-2 * ... * 1
    Donde n va disminuyendo 1 hasta ser igual a 1
    """
    return n * factorial(n - 1)

#libreria de matematicas
# import math

if __name__ == '__main__': # main del programa

    while True:

        n = int(input()) # numero de cartas

        if n == 0: # si recibimos un 0
            break # terminamos el programa

        print(factorial(n))
        """
        Modo rapido
        Aprovechando la libreria de matematicas, podemos utilizar la Funcion
        factorial en vez de escribir nuestra Funcion
        print(math.factorial(n))
        """
