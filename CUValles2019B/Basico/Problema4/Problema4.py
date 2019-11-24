"""
Problema 4: Palabra mariposa
Autor de la solucion: Luis Arturo DLG.
Python 3.x

Descripcion del problema: Dado una palabra mostrar en pantalla la figura que
simula una mariposa como se muestra en la salida

Entrada: Tinieblas

Salida:
T                T
Ti              iT
Tin            niT
Tini          iniT
Tinie        einiT
Tinieb      beiniT
Tiniebl    lbeiniT
Tiniebla  albeiniT
TinieblassalbeiniT
TinieblassalbeiniT
Tiniebla  albeiniT
Tiniebl    lbeiniT
Tinieb      beiniT
Tinie        einiT
Tini          iniT
Tin            niT
Ti              iT
T                T

Explicacion: Si observamos la figura, veremos que la figura se forma con la
aparicion de una de las letras de la palabra, para el primer renglon, tenemos
a la letra 'T', para el segundo la palabra 'Ti', y este proceso se repite por
la longitud de la palabra, y este proceso a su vez se repite de manera inversa
para formar la parte inferior. Para formar cada linea podemos considerar lo
siguiente:
1ra mitad
1/2 linea = palabra[0 -> i] + (" " * i)

Indicamos que tomaremos las letras de la posicion 0 hasta i, donde i es el renglon
a imprimir, y le vamos a sumar la cantidad de espacios para completar la
longitud de la palabra. El resultado obtenido debe de reflejarse del otro resultado
por lo que la linea seria:
linea = 1/2 linea + invertir(linea)

Esto aplica tanto para la parte superior y para la inferior, en esta ultima, recorreremos
los valores del renglon empezando desde la longitud de la palabra hasta 1.
"""

if __name__ == '__main__': # main del programa
    palabra = input() # leer la palabra
    longitud = len(palabra) # obtenemos la longitud de la palabra con len()

    """
    Parte superior
    Aplicamos la formula:
    1/2 linea = palabra[0 -> i] + (" " * i)
    linea = 1/2 linea + invertir(linea)

    Para formar la primera mitad de la mariposa, donde i ira desde 1 hasta
    longitud, la funcion range excluye el valor limite, por lo cual incrementamos
    en uno longitud.
    """
    for i in range(1, longitud + 1):
        """
        Usando los [], indicamos que queremos los caracteres desde 0 (va de manera
        implicita) hasta i -1, y concatenamos con el valor restante de longitud menos i;
        posteriormente concatenamos la cadena resultante con su inverso, usando [], le
        indicamos a Python que tome la cadena por completo (implicitamente sin colocar
        valor inicial y limita, e indicamos como paso -1, el cual invierte la cadena)
        """
        imprimir =  palabra[:i] + " " * (longitud - i)
        print(imprimir + imprimir[::-1])

    """
    Parte inferior
    Repetimos el paso anterior pero con el rango de longitud hasta 1
    """
    for i in range(longitud, 0, -1):
        
        imprimir =  palabra[:i] + " " * (longitud - i)
        print(imprimir + imprimir[::-1])
