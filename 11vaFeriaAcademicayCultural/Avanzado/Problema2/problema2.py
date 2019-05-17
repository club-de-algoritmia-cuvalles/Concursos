#La Tribu problem 2
#Yes
from sys import stdin, stdout

if __name__ == "__main__":
    palabra = stdin.readline().strip()
    espacios = len(palabra)-1
    aux = []
    for p in palabra:
        aux.append(p)
        stdout.write("{}{}\n".format(" "*espacios, "".join(aux)))
        espacios-=1
    espacios = 1
    for _ in palabra:
        aux.pop(0)
        stdout.write("{}\n".format("".join(aux)))
