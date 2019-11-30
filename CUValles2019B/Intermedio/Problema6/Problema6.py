"""
Problema 6: IPv4 Protocol
Autor de la solucion: Luis Arturo DLG.
Python 3.x

Descripcion del problema: Convertir una direccion IPv4 en decimal a su
representacion en octetos en binario.

Ejemplo:
Entrada 1:
192.168.1.254

Salida 1:
11000000101010000000000111111110

Entrada 2:
0.0.0.0

Salida 2:
00000000000000000000000000000000

Entrada 3:
255.255.255.0

Salida 3:
11111111111111111111111100000000

Explicacion: Para este problema primero sera necesario dividir la cadena por '.'
para procesar a cada octeto (cada numero dentro de una direccion ip se le llama
octeto), para posteriormente calcular su representacion en binario.

Ejemplo:
ip = 192.168.1.254
_________________________
|| decimal || binario  ||
-------------------------
|| 192     || 11000000 ||
|| 168     || 10101000 ||
|| 1       || 00000001 ||
|| 254     || 11111110 ||
-------------------------

Para calcular el binario de un numero decimal, podemos dividir entre 2 (la base
numerica del sistema binario), e ir tomando los residuos de la division para
formar la cadena:
Ejemplo:

192 | 2
  0   96 | 2
       0   48 | 2
            0   24 | 2
                 0   12 | 2
                      0   6 | 2
                          0   3 | 2
                              1   1 | 2
                                  1
Tomando los residuos del ultimo al primero, obtenemos la representacion binaria
de 192.
Nota: no siempre se completaran 8 digitos binarios, por lo que debera de 
colocar 0's en la parte izquierda del numero para completar el octeto.
"""

def decimal_a_binario(numero):
    """
    Funcion para imprimir la conversion de decimal a binario de 8 digitos
    parametros:
    > numero: int
    """
    binario = ['0'] * 8 # creamos una lista de 8 elementos, por defecto
                        # todos son '0'
    """
    En python podemos emplear indices negativos para acceder de manera invertida
    a los elementos de la lista, por ejemplo, -1 accede al elemento en la posicion
    7 de la lista binario, -2 a la posicion 6 y asi sucesivamente.
    """
    indice = -1

    while numero > 0: # mientras el numero sea mayor a 0

        binario[indice] = str(numero % 2) # asignamos el residuo de dividir
                                          # numero / 2
        numero = numero // 2 # division entera de numero entre 2
        indice -= 1 # restamos 1 al indice para acceder al sig. elemento

    for i in binario:
        print(i, end='') # impirmimos el octeto sin salto de linea


if __name__ == '__main__': # main del programa
    ip = input().split('.') # dividimos la cadena por los puntos de la ip

    for octeto in ip:

        decimal_a_binario(int(octeto))
        """
        Modo rapido
        Podemos aprovechar las f-string de python que nos deja imprimir un int en
        su representacion en binario usando el presentador 'b' de la siguiente forma:
        f{'numero:b'}
        Para poderle especificar que queremos una representacion binaria de un ancho
        de 8, debemos de colocar como prefijo a '08', donde '0' indica que el ancho
        sera rellenado con dicho caracter, y '8' como el ancho deseado.
        print(f'{octeto:08b}', end='')
        """

    print() # imprimimos un salto de linea al final del programa
