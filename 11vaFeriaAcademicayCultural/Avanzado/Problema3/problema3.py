#La Tribu problem 3
#Yes
from sys import stdin, stdout

if __name__ == "__main__":
    n = int(stdin.readline())
    a=1
    for i in range(1,n+1,2):
        espacio = [" "]*(n-a)
        a+=1
        asterisco = ["*"]*i
        stdout.write("{}{}\n".format("".join(espacio),"".join(asterisco)))
    espacio = [" "]*(n - 1)
    stdout.write("{}*\n".format("".join(espacio)))
    espacio = [" "]*(n - 2)
    asterisco = ["*"]*3
    stdout.write("{}{}\n".format("".join(espacio),"".join(asterisco)))
