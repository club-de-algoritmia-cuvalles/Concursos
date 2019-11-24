"""
Problema 3: Separar frase
Autor de la solucion: Luis Arturo DLG.
Python 3.x

Descripcion del problema:Recibiremos una frase, la cual puede contener cualquier
tipo de caracter, y debemos de separar los numeros de los demas caracteres,
y los numeros deben ser sumados

Entrada: Ae78YuPo5?8&40
Salida:
Cadena numérica 785840
Cadena no numérica: AeYuPo?&
la suma de la cadena numérica es: 32

Explicacion: Debemos de tomar toda la frase, usando 2 arreglos, debemos de mandar
en una de ellas los numeros, y en el otro los demas caracteres; se debera mostrar
el contenido de ambas listas, y convertir los caracteres numericos en int para
ser sumados
"""

if __name__ == '__main__': # main del programa
    frase = input() # leer la frase
    # Creamos 2 listas para separar los caracteres de los numeros
    numeros = []
    caracteres = []
    total = 0 # creamos un acumulador para la suma de numeros

    for caracter in frase:

        if caracter.isdigit(): # el metodo isdigit verifica si el numero es un digito
            numeros.append(caracter) # agregamos el caracter a la lista de numeros
            total += int(caracter) # convertimos el caracter a numero y lo sumamos al acumulador

        else: # si no es un digito
            caracteres.append(caracter) # agregamos el caracter a la lsita de caracteres

    """las f-strigns nos permite concatenar el contenido de caracteres usando el
    prefijo f para indicar que vamos a usarla, y colocamos entre corchetes la variable
    que queremos imprimir, tambien es posible realizar funciones dentro de estas cadenas.

    el metodo join nos deja concatenar una lista de strings, indicando un separador que los
    une"""
    print(f"Cadena numérica: {''.join(numeros)}")
    print(f"Cadena no numérica: {''.join(numeros)}")
    print(f"La suma de la cadena numérica es: {total}")
