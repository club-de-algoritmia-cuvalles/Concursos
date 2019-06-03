/*Problema 4 Palabra Piramide Girada
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
Java*/

import java.util.Scanner;

class Problema4{
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    String palabra = entrada.nextLine();

    for(int i = 1; i < palabra.length(); i++){{//for para imprimir la parte superior de la piramide
      System.out.println(palabra.substring(0, i));
    }

    for(int j = palabra.length(); j > 0; j--){//for para imprimir la parte inferior de la piramide
      System.out.println(palabra.substring(0, j));
    }
  }
}
