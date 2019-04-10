#Team Warriors Problem B
#Yes
def main():
	acbecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	numFrase = int(input())
	frases = []
	faltantes = []

	for i in range (0,numFrase):
		frases.append(input())

	for x in frases:
		falta = []
		for letra in acbecedario:
			if letra not in x:
				if letra.upper() not in x:
					falta.append(letra)
		faltantes.append(falta)

	for f in faltantes:
		if len(f)==0:
			print("pangram")
		else:
			cadena = "".join(f)
			print("missing",cadena)



if __name__ == '__main__':
	main()