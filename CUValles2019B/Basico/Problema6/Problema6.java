/*
Problema 6: Las operaciones de Nadia
Autor de la solucion: AlbertAvile.
Java 8
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
*/

import java.util.Scanner;
import java.text.DecimalFormat;

public class Problema6{
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    int casos = entrada.nextInt();

    for(int i = 0; i < casos; i++){
        float x = entrada.nextInt();
        float y = entrada.nextInt();
        char operador = entrada.next().charAt(0);

        DecimalFormat formato = new DecimalFormat("#.0");
        switch (operador) {
            case '+':
            System.out.println(formato.format(x+y));
            break;

            case '-':
            System.out.println(formato.format(x-y));
            break;

            case '*':
            System.out.println(formato.format(x*y));
            break;

            case '/':
            System.out.println(formato.format(x/y));
            break;
        }
    }

  }
}