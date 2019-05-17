#La Tribu Problem G
#Yes
from sys import stdin, stdout
import  math

if __name__ == '__main__':
    _ = int(next(stdin))
    productos = [int(i) for i in next(stdin).split()]
    q = int(next(stdin))
    for _ in range(q):
        query = int(next(stdin))
        p2g = math.ceil(productos[query-1]/5)
        stdout.write("{}\n".format(p2g))