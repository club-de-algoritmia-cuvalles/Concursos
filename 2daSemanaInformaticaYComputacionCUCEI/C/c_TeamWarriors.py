#Team Warriors Problem C
#Yes
def main():
	def calcularCuadrado(frase):
		tamFrase = len(frase)
		k = 0
		for i in range(1,101):
			if i*i >= tamFrase:
				k=i
				break
		return k
	numfrases= int(input())
	resultado = []

	for x in range(0,numfrases):
		fraseSinSeparar = input()
		k = calcularCuadrado(fraseSinSeparar)
		aux=[]
		fraseSeparada = []
		tamFrase = len(fraseSinSeparar)

		for i in range (0,k*k):
			if i%k == 0 and i != 0:
				fraseSeparada.append(aux)
				aux = []
				if i < tamFrase:
					aux.append(fraseSinSeparar[i])
				if i >= tamFrase:
					aux.append('*')
			elif i<tamFrase:
				aux.append(fraseSinSeparar[i])
			else:
				aux.append('*')
			if i == (k*k)-1:
				fraseSeparada.append(aux)
		resultado.append(fraseSeparada)

	salida = []
	for frasesota in resultado:
		salidaAux = []
		for i in range (0,len(frasesota)):
			for j in range(len(frasesota) - 1, -1, -1):
				salidaAux.append(frasesota[j][i])
		salida.append(salidaAux)

	for sal in salida:
		out=[]
		for s in sal:
			if s != '*':
				out.append(s)
		print("".join(out))

if __name__ == '__main__':
	main()