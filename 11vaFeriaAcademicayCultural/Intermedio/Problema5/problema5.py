"""Problema 5 Baker Palindromes
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
Python 2.7"""
from collections import deque
from sys import stdin

def es_palindromo(palabra):
    """Funcion para verificar si una palabra es palindromo"""
    palabra = list(palabra)
    return palabra == palabra[::-1]

if __name__ == '__main__':
    INPUT = stdin
    t = next(INPUT)
    par, pdr = False, False # booleanos para verificar si es es_palindromo antes y despues de la rotacion
    for _ in range(int(t)):
        palabra, n = next(INPUT).split()
        """Usamos la clase deque para implementar el metodo rotate, el cual
        rota n elementos a la derecha como lo requiere el problema"""
        palabra = deque(palabra)
        n = int(n)
        par = es_palindromo(palabra)
        palabra.rotate(n)
        pdr = es_palindromo(palabra)

        #  verificamos las condiciones para imprimir el mensaje correspondiente
        mensaje = {(True, True): 'Baker Palindrome',
                   (True, False): 'Palindrome',
                   (False, True): 'Possible Baker Palindrome',
                   (False, False): 'No Baker Palindrome'}.get((par, pdr))
        print(mensaje)
