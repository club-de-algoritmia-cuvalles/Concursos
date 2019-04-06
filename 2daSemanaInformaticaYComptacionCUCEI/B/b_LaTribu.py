#La Tribu Problem B
#Yes
from sys import stdin, stdout
import string

def letras_faltantes(palabra):
	letras = {letter for letter in string.ascii_lowercase}
	conj_palabra = {p for p in palabra}
	return letras - conj_palabra

if __name__ == "__main__":
	
	INPUT = iter(stdin)
	n = next(INPUT)
	for _ in range(int(n)):
		palabra = next(INPUT).lower()
		#print(palabra)
		missing = letras_faltantes(palabra)
		if missing:
			stdout.write("missing {}\n".format("".join(sorted(missing))))
		else:
			stdout.write("pangram\n")
	