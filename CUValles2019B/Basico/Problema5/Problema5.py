"""
Problema 5: My office
Autor de la solucion: Luis Arturo DLG.
Python 3.x

Descripcion del problema:Recibiremos una frase el cual sera el titulo a centrar,
y un numero entero el cual nos indicara las unidades a centar el titulo

Entrada:
My Office
15
Salida:
######################################
              My Office
######################################

Explicacion: Para lograr dar con la longitud correcta de la linea de '#'
tendremos que sumar la longitud del titulo y sumarle 2 veces las unidades
recibidas para centrar.

Y para centrar el titulo solamente se necesita colocar espacios, la cantidad
estara determinada por las unidades recibidas

Ejemplo:
longitud("My office") = 9
unidades = 15
n = longitud("My office") + (2 * unidades) = 15 + 18 = 32
###################################### : '#' * 32
              My Office
###################################### : '#' * 32
"""

if __name__ == '__main__': # main del programa
    titulo = input() # leer el titulo
    unidades = int(input()) # leer las unidades a centrar
    """Para lograr la longitud de la linea de '#' aplicamos la formula:
    n = longitud(titulo) + (2 * unidades)"""
    longitud = len(titulo) + (unidades * 2)

    # modo manual
    print("#" * longitud)  # imprimimos n veces el '#'
    print((" " * unidades) + titulo) # concatenamos los espcios con el titulo
    print("#" * longitud)

    """modo pythonico
    print("#" * longitud)
    print(titulo.center(longitud)) # el metodo center, centra el titulo en una longitud dada
    print("#" * longitud)"""
