#La Tribu Problem A
#No Time Limit Exceeded
from sys import stdin, stdout
import itertools

if __name__ == '__main__':
    n = int(next(stdin))
    alumnos = [int(a) for a in next(stdin).split()]
    suma = 0
    for i in range(n):
        for j in range(i+1, n):
            res = alumnos[j] - alumnos[i]
            if  res not in {-1,0,1}:
                suma += res

    stdout.write('{}\n'.format(suma))