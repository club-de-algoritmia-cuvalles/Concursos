"""
Problema 4: The tyrolese
Autor de la solucion: Luis Arturo DLG.
Python 3.x

Descripcion del problema: Dado la diferencia de altura entre n pares de postes y
la distancia entre ellos, calcular la cuerda para unir ambos postes de la parte
superior.

Ejemplo:
Entrada:
4
4.0 4.0
2.0 5.0
5.0 1.0
9.0 2.0

Salida:
5.657
5.385
5.099
9.22

Explicacion: Recibiremos n pares de postes con su diferencia de altura y distancia
entre ellos de la siguiente manera:
4 <- pares de postes
4.0 4.0 <- diferencia de altura | distancia entre los postes
2.0 5.0
5.0 1.0
9.0 2.0

En el ejercicio se nos muestra una imagen de como se encuentran los postes
distribuidos:
   __________
    ||\     |
    || \    | < Diferencia de altura entre P1 y P2
    ||  \ <-|-- Distancia a calcular
   _||___\ _|
    ||   ||
    ||   ||
    ||   ||
    ||   ||
    ------- < Distancia entre postes
    ^     ^
    P1    P2
Si observamos bien, los datos que nos proporciona el problema forman un triangulo
rectangulo, por lo que podemos aplicar el teorema de pitagoras para obtener la
longitud de la cuerda.

El teorema de pitagoras nos dice que la hipotenusa es el total de la raiz cuadrada
de los cuadrados de los lados del triangulo, dicho de otra forma seria:
H = (x^2 + y^2)^(1/2)

Por lo cual debemos de aplicar el teorema con todos los pares de postes para
solucionar el problema.
"""

def hipotenusa(x, y):
    """
    Funcion para calcular la hipotenusa de un triangulo dado 2 lados.
    parametros:
    > x, y: int
    retorno:
    int con el valor de la hipotenusa
    """
    return (x ** 2 + y ** 2) ** 0.5

#libreria de matematicas
#import math

if __name__ == '__main__': # main del programa
    n = int(input()) # pares de postes

    for _ in range(n):
        """
        Dividimos la entrada con split() y le asignamos el valor a cada variable
        para posteriormente convertirlo en float
        """
        altura, distancia = input().split()
        altura = float(altura)
        distancia = float(distancia)
        #Modo manual
        print(hipotenusa(altura, distancia))
        """
        Modo Rapido
        La mayoria de lenguajes provee  una libreria matematica, en ella
        viene la funcion hypot(), la cual calcula la hipotenusa de un triangulo
        print(math.hypot(altura, distancia))
        """
