#La Tribu Problem I
#No uso de funcion prohibida(?)
n = 0
while 1:
    try:
        line = raw_input()
        div = int(line)
        if not div % 3: n+=1
    except EOFError:
        break
           
print n