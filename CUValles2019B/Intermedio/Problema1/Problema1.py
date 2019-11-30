"""
Problema 1: 'La gusga' dispensers
Autor de la solucion: Luis Arturo DLG.
Python 3.x

Descripcion del problema: El problema consiste en hacer
un conteo de los productos de la dispensadora, si hay
producto debemos de mostrar el mensaje:
There are n products of x
Donde n es la cantidad de productos y x el producto solicitado.
Si no hay producto debemos de mostrar el mensaje:
Product x is sold out.

Ejemplo:
Entrada:
10
A B C A A E E C D D
2
A
F
Salida:
There are 3 products of A
Product F is sold out

Explicacion:
La entrada nos indica en el primer renglon que recibiremos n productos
los cuales se pueden repetir a lo largo de la siguiente linea;
posteriormente se nos indicaran los productos a recibir.

Ejemplo:
10 <- Numero de productos
A B C A A E E C D D <- Productos separados por espacio
2 <- Numero de productos a buscar
A <- Producto a buscar
F

Para resolver el problema deberemos de convertir la cadena separada
por espacios en una lista, para posteriormente hacer un conteo de los
elementos indicados.
Ejemplo:
Producto a buscar: A
            1        2  3            <- Conteo
Productos: [A, B, C, A, A, E, C, D, D]
Para A tenemos 3 productos.
En el caso de F, como podemos ver no hay producto alguno.
"""

def busqueda_productos(dispensadora, producto):
    """
    Funcion para contar las apariciones de un producto en la dispensadora.
    parametros:
    > dispensadora = List[str]
    > producto = str
    retorno:
    int con la cantidad de productos encontrados
    """
    cantidad = 0 # variable contadora

    for p in dispensadora:

        if producto == p: # si el producto que buscamos es igual a p
            cantidad +=1 # sumamos 1 al contador

    return cantidad # retornamos la cantidad de productos


if __name__ == '__main__': # main del programa
    """
    Nota: en python no es necesario saber cuantos elementos debemos recibir
    para formar listas, pero se deben de leer las entradas si se ha especificado
    en el problema.
    """
    n = int(input()) # numero de productos en la dispensadora
    """
    Para obtener una lista de los elementos separados por espacio, podemos usar
    metodo split para generar una lista con el espacio como separador por
    default
    """
    dispensadora = input().split() # lista de Productos

    #modo manual
    q = int(input()) # numero de productos a buscar
    for _ in range(q):

        producto = input()
        cantidad_producto = busqueda_productos(dispensadora, producto)

        """
        Modo Pythonico:
        list tiene un metodo llamado count, el cual puede contar los elementos
        al igual que la funcion busqueda_productos();

        cantidad_producto = dispensadora.count(producto)
        """

        if cantidad_producto > 0: # Si hay producto
            print(f"There are {cantidad_producto} products of {producto}")

        else: # Si no hay producto
            print(f"Product {producto} is sold out")
