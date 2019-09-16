#La Tribu Problem I
#No Time Limit Exceeded
from sys import stdin, stdout
import functools
import math

@functools.lru_cache(maxsize=100000)
def factorial(n):
    f = math.factorial(n)
    return int(str(f).rstrip('0'))


if __name__ == '__main__':
    n = next(stdin)
    for _ in range(int(n)):
        l, r, x, y = (int(i) for i in next(stdin).split())
        acumulador = 0
        for a in range(l, r+1):
            fact = factorial(a)
            if x<= fact <=y:
                acumulador+=1

        stdout.write("{}\n".format(acumulador))
