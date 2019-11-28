/*
Problema 5: My office
Autor de la solucion: AlbertAvile.
Java 8
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
*/

import java.util.Scanner;

public class Problema5{
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    String cadena = entrada.nextLine();
    int unidades = entrada.nextInt();
    
    for(int i = 0; i < cadena.length()+(unidades*2); i++){
      System.out.print("#");
    }
    System.out.println();

    for(int i = 0; i < unidades; i++){
      System.out.print(" ");
    }
    System.out.println(cadena);

    for(int i = 0; i < cadena.length()+(unidades*2); i++){
      System.out.print("#");
    }
    System.out.println();
  }
}