"""
Problema 6: Las operaciones de Nadia
Autor de la solucion: Luis Arturo DLG.
Python 3.x

Descripcion del problema:Recibiremos n operaciones, las cuales vamos a tener que
resolver con los 2 numeros que recibimos y el operador que vienen en la linea

Entrada:
4
45 89 +
32 16 –
30 7 *
160 40 /

Salida:
134.0
16.0
210.0
4.0

Explicacion: El primer numero nos va a indicar la cantidad de operaciones que recibiremos,
en cada renglon vendra las operaciones que debemos de realizar, con los 2 numeros y el
operador, este problema se puede resolver con seleccion multiple

Ejemplo:
4 -> indica las lineas a recibir
45 89 + = 45 + 89 = 134.0
32 16 – = 32 - 16 = 16.0
30 7 * = 30 * 7 = 210.0
160 40 / = 160 / 40 = 4.0
"""
# libreria con funciones de operadores (+, -, *, /)
#import operator

if __name__ == '__main__': # main del programa
    casos = int(input())

    """
    El guion bajo significa que ignoraremos los numeros generados por
    range()
     """
    for _ in range(casos):

        """
        input recibe toda entrada como cadena a diferencia de C/C++ Y Java
        que pueden definir que tipo de dato recibira, por lo cual, se uso el
        metodo split, para separar los datos por el espacio en blanco, para asi
        asignarlos en 3 variables. Ejemplo
        entrada: '45 89 +'
        x, y, operador = input.split()
        x = '45'
        y = '89'
        operador = '+'
        Nota: tanto x, como y siguen siendo de tipo str, por lo que se debe de
        hacer conversion a int
        """
        x, y, operador = input().split()
        x, y = int(x), int(y)

        # modo manual
        if operador == '+':
            """
            En python podemos redondear a un decimal usando la notacion .nf, donde
            n es la cantidad de digitos al usar, es similar a %nf que se puede usar
            en la instruccion printf de C
            """
            print(f"{x + y:.1f}")

        elif operador == '-':
            print(f"{x - y:.1f}")

        elif operador == '*':
            print(f"{x * y:.1f}")

        elif operador == '/':
            print(f"{x / y:.1f}")

        """
        modo pythonico
        Python carece de la sentencia switch - case, pero se puede emular usando
        la clase dict, usando el metodo get(), podemos buscar dentro de este la
        funcion del modulo operator en cuestion; y se invoca con 'x' y 'y' de
        argumentos para obtener el resultado
        resultado = {"+": operator.add,
                     "-": operator.sub,
                     "*": operator.mul,
                     "/": operator.truediv}.get(operador)(x, y)
        print(f"{resultado:.1f}")
        """
