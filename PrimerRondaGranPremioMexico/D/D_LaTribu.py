#La Tribu Problem D
#No Time Limit Exceeded
from sys import stdin, stdout
import collections
import heapq

def dijsktra(grafo, origen, final):
    rutas = []
    Ruta = collections.namedtuple('Ruta', 'peso nodo')
    for vertice in grafo[origen]:
        heapq.heappush(rutas, Ruta(1,[vertice]))

    visitados = set([origen])

    while True:
        peso, path =  heapq.heappop(rutas)
        nodo = path[-1]
        if nodo in visitados:
            continue
        if nodo is final:
            return [origen]+path

        for v in grafo[nodo]:
            nuevo_peso = peso + 1
            new_path = path + [v]
            heapq.heappush(rutas, Ruta(nuevo_peso, new_path))

        visitados.add(nodo)

if __name__ == '__main__':
    v, e = (int(i) for i in next(stdin).split())
    code = {str(vertice):c for vertice,c in enumerate(next(stdin).split(),1)}
    grafo_rally = collections.defaultdict(set)

    for _ in range(v-1):
        o, d = next(stdin).split()
        grafo_rally[o].add(d)
        grafo_rally[d].add(o)

    for _ in range(e):
        origen, destino = next(stdin).split()
        t_code = dijsktra(grafo_rally, origen, destino)
        stdout.write("{}\n".format(''.join(code[c] for c in t_code)))
