#La Tribu Problem I
#No Time Limit Excceded
from sys import stdin, stdout

def isSubsetsum(conjunto, n, suma, o):
    if suma == 0:
        return True
    if n == 0 and suma!=0:
        return False
    if conjunto[n-1] > suma:
        return isSubsetsum(conjunto, n-1, suma,o)
    o.add(suma)
    return isSubsetsum(conjunto, n-1, suma,o) or isSubsetsum(conjunto, n-1, suma-conjunto[n-1],o)

if __name__ == '__main__':
    n = int(next(stdin))
    conjunto = [int(i) for i in next(stdin).split()]
    sumas_obtenidas = set(conjunto)
    hn = 1
    while True:
        if not hn in sumas_obtenidas and not isSubsetsum(conjunto, n, hn,sumas_obtenidas):
            stdout.write("{}\n".format(hn))
            break
        hn+=1
