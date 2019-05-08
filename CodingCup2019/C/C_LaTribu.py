#La Tribu problem C
#No enviado/incompleto
R,C = map(int, input().split())
tele = []

for n in range(R):
    tele.append(list(input()))
mx=0
mn=90000

t=0
while t<R:
    
    r=0
    aux=0
    mul=1
    while r<C:
        if tele[t][r]=="X":
            tele[t][r]="R"
            aux +=1
            while r<C:
                r+=1
                if tele[t][r]=="X":
                    aux+=1
                    tele[t][r]="R"
                else:break
            for abajo in range(t+1,R):
                if tele[abajo][r]=="X":
                    tele[t][r:r+aux]="R"*aux
                    mul+=1
                else:break
            if mx<(aux*mul):
                mx=(aux*mul)
            if mn>(aux*mul):
                mn=(aux*mul)
        aux=0
        mul=1
            
        r+=1
    t+=1
            
    