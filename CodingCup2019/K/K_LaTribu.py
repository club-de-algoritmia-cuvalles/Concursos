#La Tribu Problem K
#Aceptado(100)
trie = {}

def agregar(palabra, valor):
    aux = trie
    for letra in palabra:
        aux = aux.setdefault(letra, {})
        try:
            aux["#"]+=1
            aux["valores"].add(valor)
        except KeyError:
            aux["#"] = 1
            aux["valores"] = set([valor])
    aux.setdefault("end","end")
    aux["valor"] = valor

def valor_maximo(prefijo):
    vm, cant = 0, 0
    aux = trie
    for letra in prefijo:
        aux = aux[letra]
    cant = aux["#"]
    vm = max(aux["valores"])

    return cant, vm

#### aqui inicia
for _ in range(int(raw_input())):
    palabra = raw_input()
    valor = int(raw_input())
    agregar(palabra, valor)

for _ in range(int(raw_input())):
    prefijo = raw_input()
    v,c = valor_maximo(prefijo)
    print v, c
    
from pprint import pprint
pprint(trie)
