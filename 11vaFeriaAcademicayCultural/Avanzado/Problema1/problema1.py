#La Tribu problem 1
#Yes
from sys import stdin, stdout

if __name__ == "__main__":
    palabra = stdin.readline().strip()
    if 5> len(palabra) >17 or palabra[0].isdigit():
        stdout.write("Invalid password\n")
    else:
        cont_digitos = 0
        band_M = False
        correcto = True
        band_A = False
        for i, p in enumerate(palabra):
            if p.isupper():
                band_M = True

            if p.isalpha():
                band_A = True
            
            if p.isdigit():
                try:
                    if p!= palabra[i+1]:
                        cont_digitos += 1
                    else:
                        correcto = False
                        break
                except IndexError:
                    cont_digitos += 1

            if p == " " or p == "/":
                correcto = False
                break

        if correcto and band_M and band_A and (0 < cont_digitos < 5):
            stdout.write("Valid password\n")

        else:
            stdout.write("Invalid password\n")

            

            
