#La Tribu problem 6
#Yes
from sys import stdin, stdout

if __name__ == "__main__":
    palabra = stdin.readline().strip()
    palabra = palabra.replace("Coins = [","")
    palabra = palabra.replace("]","")
    palabra = palabra.replace(" amount = ","")
    monedas = [int(i) for i in palabra.split(",")]
    monto = monedas.pop()
    monedas.sort(reverse=True)
    monedero = 0
    while monto and monedas:
        mg = monedas[0]
        if monto - mg >= 0:
            monto-=mg
            monedero+=1

        else:
            monedas.pop(0)

    if not monto:
        stdout.write("{}\n".format(monedero))
    else:
        stdout.write("-1\n")
            

            
