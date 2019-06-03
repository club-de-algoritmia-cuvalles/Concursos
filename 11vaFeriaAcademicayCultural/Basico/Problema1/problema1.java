/*Problema 1 Contador Ascendente o Descendente
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
Java*/

import java.util.Scanner;

class Problema1{
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    int inferior = entrada.nextInt();
    int superior = entrada.nextInt();

    /*Comparamos si el limite inferior es menor al superior, de ser asi, nuestra Secuencia
    es ascendente, de lo contrario es descendente, al imprimri omitimos el salto de linea y dejamos
    un espacio despues de imprimir cada numero*/
    if(inferior < superior){ // Secuencia incremental
      for(int i = inferior; i <= superior; i++){
        System.out.print(i+" ");
      }
      System.out.println();
    }
    else{ // Secuencia decremental
      for(int j = inferior; j >= superior; j--){
        System.out.print(j+" ");
      }
      System.out.println();
    }
  }
}
