#La Tribu Problem C
#No Send
from sys import stdin, stdout

if __name__ == '__main__':
    t = int(next(stdin))
    for case in range(t):
        nc = int(next(stdin))
        sp = {(i,j) for i,j in enumerate(range(2, nc+1),1)}
        nr = int(next(stdin))
        sc = set()
        for r in range(nr):
            origen, destino, _ = (int(i) for i in next(stdin).split())
            sc.add((origen, destino))
        cf = sp - sc
        b = True if cf else False
        costo = 0
        ncc = int(next(stdin))
        for _ in range(ncc):
            o, d, c = (int(i) for i in next(stdin).split())
            if cf and (o,d) in cf:
                costo += c
                cf.remove((o,d))
        if not b:
            stdout.write('Thank you, Goodbye\n')
        elif not cf:
            stdout.write('{}\n'.format(costo))
        else:
            stdout.write('You better hire someone else\n')






