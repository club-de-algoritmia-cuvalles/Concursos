/*Problema 4 Without Repetitions
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
Java*/

import java.util.ArrayList;
import java.util.Scanner;

class Problema4{
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    String oracion = entrada.nextLine();
    ArrayList<Character> nuevaOracion = new ArrayList<Character>();//Array para la nueva oracion
    char caracterActual = oracion.charAt(0);//bandera para verificar si hemos insertado una letra mayuscula
    boolean mayuscula = Character.isUpperCase(caracterActual);//variable para comparar las repeticiones contiguas
    nuevaOracion.add(caracterActual);
    for(int i = 1; i < oracion.length(); i++){//iniciamos del 2do caracter
      char caracter = Character.toLowerCase(oracion.charAt(i));
      if(caracter != caracterActual){
        if(Character.isUpperCase(oracion.charAt(i)) && !mayuscula){
          caracter = Character.toUpperCase(caracter);//cambiamos el caracter a mayuscula para insertarlo en la lista
          mayuscula = true;
        }
        nuevaOracion.add(caracter);
        caracterActual = caracter;
      }
    }
    for(int j = 0; j < nuevaOracion.size(); j++){System.out.print(nuevaOracion.get(j));}
    System.out.println();
  }
}
