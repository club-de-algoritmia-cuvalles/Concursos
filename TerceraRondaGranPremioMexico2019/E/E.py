from sys import stdin, stdout

if __name__ == '__main__':
    n = int(next(stdin))
    machos, tanque_optimo = 0, 0
    for _ in range(n):
        m, f = map(int, next(stdin).split())
        machos += m
        tanque_optimo = min(f, m)

    # print(tanque_optimo, machos)

    stdout.write(f'{machos + tanque_optimo}\n')
