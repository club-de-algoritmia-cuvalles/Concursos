"""Problema 4 Without Repetitions
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
Python 2.7"""

"""el uso del modulo sys para entrada/salida de datos es altamente recomendado en programacion
competitiva (ojo: no todas las competencias permiten su uso), pero puede usar los metodos
propios definidos en python (raw_input y print)"""
from sys import stdin, stdout

if __name__ == '__main__':
    oracion = stdin.readline().decode("utf8") #  decodificamos los carcateres de utf8 para manipularnos
    nueva_oracion = [] #  lista para la nueva oracion
    mayuscula = oracion[0].isupper() # bandera para verificar si hemos insertado una letra mayuscula
    caracter_actual = oracion[0] #  variable para comparar las repeticiones contiguas
    nueva_oracion.append(caracter_actual)
    for _caracter in oracion[1:]: #  iniciamos del 2do caracter
        caracter = _caracter.lower() #  convertimos el caracter a minuscula para comparar
        if caracter != caracter_actual:
            if _caracter.isupper() and not mayuscula:
                caracter = caracter.upper() #  cambiamos el caracter a mayuscula para insertarlo en la lista
                mayuscula = True
            nueva_oracion.append(caracter)
            caracter_actual = caracter
    #  codificamos los carcateres de utf8 para imprimir la cadena final
    stdout.write('{}'.format(''.join(nueva_oracion).encode("utf8")))
