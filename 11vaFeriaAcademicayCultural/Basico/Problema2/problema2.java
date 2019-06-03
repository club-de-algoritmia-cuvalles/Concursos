/*Problema 2 Solo numeros
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
Java*/

import java.util.Scanner;

class Problema2{
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    String cadena = entrada.nextLine();
    int acumulador = 0; //inicializamos un acumulador para almacenar el valor de los numeros

    for(int i = 0; i < cadena.length(); i++){
      char elemento = cadena.charAt(i); // accedemos al caracter en el indice i
      if(Character.isDigit(elemento)){// verificamos si es digito con isDigit de Character
        /*convertimos al caracter en numero con el metodo parseInt de la clase Interger
        forzando al caracter a ser un String, dado que el tipo de dato que acepta dicho metodo*/
        acumulador += Integer.parseInt(""+elemento);
      }
    }
    System.out.println(acumulador);
  }
}
