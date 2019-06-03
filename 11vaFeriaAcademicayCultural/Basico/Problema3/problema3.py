"""Problema 3 Validando Password
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
Python 2.7"""

"""el uso del modulo sys para entrada/salida de datos es altamente
recomendado en programacion competitiva (ojo: no todas las competencias
permiten su uso), pero puede usar los metodos propios definidos en
python (raw_input y print)"""

from sys import stdin, stdout

if __name__ == '__main__':
    #  el metodo readline de stdin lee la siguiente linea de la entrada
    #  incluyendo el salto de linea, para eliminarlo usamos el metodo strip (sin parametros)
    #  de la clase str para eliminar los caracteres no deseados (espacios y saltos de linea)
    password = stdin.readline().strip()
    password_valido = False #  bandera booleana para validar password, inicia en False
    #  Validamos que password no inicie con un digito para ser valido
    #  ademas que su longitud sea entre 5 a 13
    if not password[0].isdigit() and 5 <= len(password) <= 13 :
        for caracter in password[1:]:
            if caracter.isdigit():
                #  si encontramos un digito dejamos de iterar y validamos el password
                password_valido = True
                break

    if password_valido:
        stdout.write('Password valido\n')
    else:
        stdout.write('Password invalido\n')
