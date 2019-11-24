"""
Problema 1: Repetir cadena numerica
Autor de la solucion: Luis Arturo DLG.
Python 3.x

Descripcion del problema:
Recibiremos una cadena de numeros de cualquier longitud
y deberemos de imprimir el digito n + 1 veces si se encuentra
en una posicion par (0 es par), y n - 1 veces si se encuentra
en una posicion impar.

Ejemplo:
Entrada: 7245314
Salida:
88888888
1
55555
4444
4444
0
55555

Explicacion: debemos de guardar el numero como una cadena para poder recorrerla;
las posiciones para el ejemplo anterior seria el siguiente

============================================
SIMBOLOGIA: P = par, I = impar            ||
============================================
paridad : P || I || P || I || P || I || P ||
============================================
posicion: 0 || 1 || 2 || 3 || 4 || 5 || 6 ||
============================================
numero  : 7 || 2 || 4 || 5 || 3 || 1 || 4 ||
============================================


Para el caso de tener una posicion par nosotros vamos a sumar uno al numero.
Ejemplo:
posicion: 0, numero: 7
numero = 7 + 1 = 8
Y como salida debemos de imprimir 8 veces el numero 8 de la siguiente manera:
88888888

Para el caso de tener una posicion impar nosotros vamos a restar uno al numero.
Ejemplo:
posicion: 1, numero: 2
numero = 2 - 1 = 1
Y como salida debemos de imprimir 1 vez el numero 1 de la siguiente manera:
1
"""

if __name__ == '__main__': # main del programa
    numero = input() # leer la cadena de numeros

    """
    Recorremos la cadena numero usando la funcion enumerate();
    la funcion enumerate nos devuelve la tupla con el indice
    y el elemento a recorrer. Ejemplo:
    numero = 7245314
    indice || digito
    0      || 7
    1      || 2
    2      || 4
    3      || 5
    4      || 3
    5      || 1
    6      || 4
    """
    for indice, digito in enumerate(numero):

        digito = int(digito)

        if indice % 2 == 0: # Si el indice es par
            digito += 1 # sumamos 1 al digito
            print(str(digito) * digito) # imprimimos el digito la misma cantidad

        else: # Si el indice es impar
            digito -= 1
            
            if digito == 0: # Si el resultado es 0, se debe de imprimir un cero
                print(0)

            else:
                print(str(digito) * digito) # imprimimos el digito la misma cantidad
