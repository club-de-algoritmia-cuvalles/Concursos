#La Tribu Problem B
#Yes
from sys import stdin, stdout

if __name__ == '__main__':
    candidatos = int(next(stdin))
    carlos = int(next(stdin))
    ganador = 'S'
    for _ in range(candidatos-1):
        candidato = int(next(stdin))
        if candidato > carlos:
            ganador = 'N'
    stdout.write('{}\n'.format(ganador))