"""
Problema 2: Iniciales en Minusculas
Autor de la solucion: Luis Arturo DLG.
Python 3.x

Descripcion del problema:Recibiremos una frase, la cual las iniciales de
cada palabra deben ser convertidas en minusculas, y el resto de la palabra en
mayusculas

Entrada: The dArK SidE oF tHe MoOn
Salida: tHE dARK sIDE oF tHE mOON

Explicacion: Debemos de tomar toda la frase (incluyendo espacios en blanco), e
ir cambiando a minusculas a las letras que inician la palabra, esto se puede hacer
buscando los espacios en blanco, una vez que encontramos la inicial, convertimos
a toda letra a mayusculas, esto hasta encontrar otro espacio y repetimos la accion
para toda la frase.
"""

if __name__ == '__main__': # main del programa
    frase = input() # leer la frase
    """Tendremos una variable de tipo booleano a manera de bandera para indicar
    si la letra que vamos a convertir es inicial o no, esta condicion siempre inicia
    en True, una vez encontrado la inicial se cambia a False, hasta encontrar un espacio"""
    inicial = True

    # Modo manual
    for letra in frase:

        if inicial: # si encontramos la inicial
            print(letra.lower(), end="") # el metodo lower convierte en minuscula la letra
            inicial = False # cambiamos la bandera a False

        else: # si no es la inicial
            print(letra.upper(), end="") # el metodo upper convierte en mayuscula a la letra

        if letra.isspace(): # el metodo isspace devuele True si el caracter es un espacio
            inicial = True # cambiamos la bandera a True

    print() # colocamos un print vacio para tener un salto de linea

    """Modo pythonico
    print(frase.title().swapcase())"""
