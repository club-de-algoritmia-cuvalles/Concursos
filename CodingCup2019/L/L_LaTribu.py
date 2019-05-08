#La Tribu Problem L
#Aceptado(100)
from collections import OrderedDict
eneagrama = OrderedDict()
n = int(raw_input())

for _ in range(n):
    personalidad = raw_input()
    eneagrama[personalidad] = OrderedDict({"Compatibles": [], "Incompatibles": [], "Alas": []})
    
for key in eneagrama.keys():
    eneagrama[key]["Compatibles"].extend(raw_input().split())
    
for key in eneagrama.keys():
    eneagrama[key]["Incompatibles"].extend(raw_input().split())
    
for key in eneagrama.keys():
    eneagrama[key]["Alas"].extend(raw_input().split())
    
n_queries = int(raw_input())

for i in range(1, n_queries+1):
    query = raw_input().split()
    try:
        if len(query) == 2:
            r, p = query
            resp = eneagrama[p][r]
        else:
            r, p1, p2 = query
            r1 = eneagrama[p1][r]
            r2 = eneagrama[p2][r]
            resp = set(r1)&set(r2)
            if not resp: resp = ["Ninguno"]
        print("Respuesta {}: {}".format(i, " ".join(resp)))
    except KeyError:
        resp = "Ninguno"
        print("Respuesta {}: {}".format(i, resp))