"""Problema 3 Bridge
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
Python 2.7"""

"""el uso del modulo sys para entrada/salida de datos es altamente recomendado
en programacion competitiva (ojo: no todas las competencias permiten su uso),
pero puede usar los metodos propios definidos en python (raw_input y print)"""
from sys import stdin

def npop(lista, n = 1):
    for _ in xrange(n):
        yield lista.pop()

if __name__ == '__main__':
    n = int(stdin.readline())
    velocidad_personas = [int(stdin.readline()) for _ in xrange(n)]
    velocidad_personas.sort(reverse=True)
    tiempo, personas, cruces = 0, [], []

    while True:
        ida = list(npop(velocidad_personas, 2))
        personas.extend(ida)
        tiempo += max(ida)
        cruces.append('{} {}'.format(*ida))
        #personas.sort(reverse=True)
        vuelta = personas.pop()
        if not velocidad_personas: break
        tiempo += vuelta
        cruces.append('{}'.format(vuelta))
        velocidad_personas.insert(0, vuelta)

    print(tiempo)
    for cruce in cruces:
        print(cruce)
