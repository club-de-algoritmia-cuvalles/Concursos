"""Problema 1 Cesar Secret
Propuesta de solucion
autor: Efrain Esau Martinez Macias
Python 2.7"""
def obtener_mensaje_desencriptado(mensaje, clave):
	salida=[] # arreglo para el mensaje desencriptado
	for p in mensaje:
		aux = ord(p) # obtener el valor ascii de la letra
		aux-=clave # le restamos 3 al valor ascii del mensaje encriptado
		if aux<97 : aux+=26
		if aux<97 or aux >122: salida.append(" ")
		else: salida.append(str(chr(aux))) #agremamos la letra a la lista convertida en str a partir del valor ascii
	return salida

def main():
	n = int(raw_input()) # numero de casos
	for _ in range(n):
		mensaje = raw_input()
		clave = 3
		salida2=obtener_mensaje_desencriptado(mensaje, clave)
		print('{}'.format("".join(salida2)))

if __name__ == '__main__':
	main()
