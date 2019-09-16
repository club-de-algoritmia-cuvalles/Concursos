#La Tribu Problem H
#Yes
from sys import stdin, stdout
from math import ceil

if __name__ == '__main__':
    vueltas, signos = map(int, next(stdin).split())
    porcentaje = (vueltas*signos)/10
    suma = 0
    for i in range(8):
        suma += porcentaje
        stdout.write('{} '.format(ceil(suma)))
    stdout.write('{}\n'.format(ceil(suma+porcentaje)))