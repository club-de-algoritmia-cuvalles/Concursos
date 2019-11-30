"""
Problema 3: Happy numbers
Autor de la solucion: Luis Arturo DLG.
Python 3.x

Descripcion del problema: Determinar si el numero que recibimos es feliz o no

Ejemplo 1:
Entrada:
19

Salida:
Yes

Ejemplo 2:
Entrada:
4

Salida:
No

Explicacion: Para determinar si un numero es feliz o no, debemos de tomar sus
digitos y sumar sus cuadrados, debemos de repetir el proceso con el resultado
obtenido hasta que la suma total sea 1 o que algun resultado (o el propio nuemro)
se repita. Para lograr esto, es necesario que almacenemos los resultados en alguna
estructura como una lista, preferentemente un conjunto para obetener una busqueda mas
rapida de los elementos.

Ejemplo 1:
> 19
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
19 cumple con la condicion para ser feliz

Ejemplo 2:
> 4
4^2 = 16
1^2 + 6^2 = 37
3^2 + 7^2 = 58
5^2 + 8^2 = 89
8^2 + 9^2 = 145
1^2 + 4^2 + 5^2 = 42
4^2 + 2^2 = 20
2^2 + 0^2 = 4 <-
4 vuelve a aparecer en los resultados, por lo cual, no es feliz

Nota: los numeros que se generan en la operacion son felices o no, dependiendo
el resultado obtenido.
"""

def suma_digitos(numero):
    """
    Funcion para sumar el cuadrado de los digitos de un numero
    parametros:
    > numero: str
    retorno:
    str con la cadena del valor de la suma
    """
    suma = 0
    for digito in numero:
        suma += int(digito) ** 2
    return str(suma)

def es_feliz(numero):
    """
    Funcion que retorna si un numero es feliz o no
    parametros:
    > numero: str
    retorno:
    bool si es feliz o no
    """
    resultados = {numero}
    while True:
        resultado =  suma_digitos(numero)
        if resultado in resultados:
            return False
        if resultado == '1':
            return True
        resultados.add(resultado)
        numero = resultado


if __name__ == '__main__': # main del programa
    """
    Para este problema, no es necesario convertir el numero a un tipo numerico,
    manejarlo como un string resulta mas sencillo para recorrer sus digitos.
    """
    numero = input() # numero de productos en la dispensadora
    if es_feliz(numero):
        print('Yes')
    else:
        print('No')
