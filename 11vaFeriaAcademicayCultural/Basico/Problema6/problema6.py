"""Problema 6 Lenguaje de la F
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
Python 2.7"""

from sys import stdin, stdout

if __name__ == '__main__':
    #  el metodo readline de stdin lee la siguiente linea de la entrada
    #  incluyendo el salto de linea, para eliminarlo usamos el metodo strip (sin parametros)
    #  de la clase str para eliminar los caracteres no deseados (espacios y saltos de linea)
    accion = stdin.readline().strip()
    mensaje = stdin.readline().strip()
    vocales = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} #  conjunto para identificar las vocales
    nuevo_mensaje = [] #  lista para crear el nuevo mensaje
    ignorar = 0
    for letra in mensaje:
        if not ignorar: #  si ignorar es mayor a cero (en Python, el valor booleano de 0 es False)
            nuevo_mensaje.append(letra)
            if letra in vocales: #  realizamos una busqueda de la letra entre las vocales, el cual es
                                 #  letra en la cual se basa el lenguaje de la F
                if accion == 'E':
                    """Si la accion es encriptar, debemos de agregar en la lista despues de la vocal la letra f, seguido de la
                    vocal encontrada en minuscula"""
                    nuevo_mensaje.extend(['f', letra.lower()])
                else:
                    """Si la accion es desencriptar, debemos de ignorar las siguientes 2 letras despues de la vocal"""
                    ignorar = 2
        else:
            ignorar-=1 #  restamos en 1 a cada iteracion para solo ignorar 2 letras

    stdout.write('{}\n'.format(''.join(nuevo_mensaje)))
