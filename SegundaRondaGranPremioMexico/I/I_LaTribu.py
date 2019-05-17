#La Tribu Problem I
#Yes
from sys import stdin, stdout
import  math

if __name__ == '__main__':
    N, M, T, t, r = (int(i) for i in next(stdin).split())
    c = 0
    d2 = 0
    for d in range(1,N+1):
        d2+=1
        if c + t <= T:
            c+=t
            M-=1
        else:
            c-=r
        if M==0:
            stdout.write("{}\n".format(d2))
            break
        if c < 0:
            c=0
    else:
        stdout.write("-1\n")