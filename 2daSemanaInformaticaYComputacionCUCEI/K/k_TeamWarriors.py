#Team Warriors Problem K
#No send

def main():
    dividendo = int(input())
    contador=0
    for i in range(1,int(dividendo/2)+1):
        if dividendo%i == 0:
            contador+=1
    contador+=1
    print(contador)

if __name__ == '__main__':
    main()