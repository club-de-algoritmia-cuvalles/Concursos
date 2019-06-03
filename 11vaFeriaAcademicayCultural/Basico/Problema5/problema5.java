/*Problema 5 Buscando un caracter
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
Java*/

import java.util.Scanner;
import java.util.ArrayList;

class Problema5{
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    String palabra = entrada.nextLine();
    char caracterBuscado = entrada.nextLine().charAt(0); // declaramos como char al caracter buscado
    ArrayList<Integer> indices = new ArrayList<Integer>(); // implementamos un ArrayList para almacenar los indices

    for(int i = 0; i < palabra.length(); i++){//for para imprimir la parte superior de la piramide
      if(palabra.charAt(i) == caracterBuscado){
        indices.add(i);
      }
    }

    System.out.print("Ese caracter se encontro en las posiciones: ");
    for(int j = 0; j < indices.size(); j++){System.out.print(indices.get(j) + " ");}
    System.out.println("\nSe encontraron " + indices.size() + " caracteres con la letra " + caracterBuscado);
  }
}
