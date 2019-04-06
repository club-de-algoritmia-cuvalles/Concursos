#La Tribu Problem A
#Yes
from sys import stdin, stdout

if __name__ == "__main__":
	vocales = {"a","e","i","o","u"}
	INPUT = iter(stdin.read().split())
	n = next(INPUT)
	for _ in range(int(n)):
		palabra = next(INPUT)
		cont_vocales = 0
		for p in palabra:
			if p in vocales: cont_vocales +=1

		stdout.write("{}\n".format(palabra))
		if cont_vocales > len(palabra)/2:
			stdout.write("1\n".format(palabra))
		else:
			stdout.write("0\n".format(palabra))
