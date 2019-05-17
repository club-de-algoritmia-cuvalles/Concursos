#La Tribu problem 5
#Yes
from sys import stdin, stdout

if __name__ == "__main__":
    palabra = stdin.readline().strip()
    longitud = 0
    inicio, final = 0, 0 
    for i, c in enumerate(palabra):
        if c == "(":
            inicio = i
            break
    for j, c in enumerate(palabra[::-1]):
        if c == ")":
            final = len(palabra)-j
            break
    cont_a = palabra.count("(",inicio,final)
    cont_b = palabra.count(")",inicio,final)
    if cont_a > cont_b:
        for i, c in enumerate(palabra[inicio+1:], 1):
            if c == "(":
                inicio += i
                break
    elif cont_a < cont_b:
        for j, c in enumerate(palabra[inicio:final-1][::-1], 1):
            if c == ")":
                final -= j
                break
    stdout.write("{}".format(final - inicio))
    
