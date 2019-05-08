#La Tribu Problem H
#Yes
from sys import stdin, stdout
import heapq

def aprovechar(problemas, tolerancia):
    tolerancia_usada = 0
    problemas_usados = 0
    for problema in problemas:
        if tolerancia_usada+problema  < tolerancia:
            tolerancia_usada += problema
            problemas_usados+=1
    return problemas_usados

if __name__ == '__main__':
    n, t = (int(i) for i in next(stdin).split())
    problemas = [int(p) for p in next(stdin).split()]
    problemas.sort()
    pf = aprovechar(problemas[::-1], t)
    sf = aprovechar(problemas[:], t)

    stdout.write('{} {}\n'.format(pf, sf))

