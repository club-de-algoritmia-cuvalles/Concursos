#La Tribu Problem C
#Yes
from sys import stdin, stdout
import math

def encriptado(palabra):
	long_palabra = len(palabra)
	tam_celda = math.ceil(math.sqrt(long_palabra))
	encriptar = []
	i = 0
	for r in range(tam_celda):
		encriptar.append(palabra[i:tam_celda+i])
		i += tam_celda

	nueva_palabra = []

	for j in range(tam_celda):
		for celda in encriptar[::-1]:
			try:
				nueva_palabra.append(celda[j])
			except IndexError:
				pass

	return nueva_palabra


if __name__ == "__main__":
	
	INPUT = iter(stdin)
	n = next(INPUT)
	for _ in range(int(n)):
		palabra = next(INPUT).strip()
		encrypted = encriptado(palabra)
		stdout.write("{}\n".format("".join(encrypted)))