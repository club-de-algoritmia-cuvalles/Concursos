/*Problema 5 Buscando un caracter
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
Java*/

import java.util.Scanner;
import java.util.ArrayList;

class Problema6{
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    char accion = entrada.nextLine().charAt(0); // declaramos como char al caracter buscado
    String mensaje = entrada.nextLine();
    int ignorar = 0;
    ArrayList<Character> nuevoMensaje = new ArrayList<Character>(); // implementamos un ArrayList para almacenar los caracteres
                                                                    //del nuevo mensaje
    for(int i = 0; i < mensaje.length(); i++){//for para imprimir la parte superior de la piramide
      if(ignorar == 0){
        char letra = mensaje.charAt(i);
        nuevoMensaje.add(letra);
        if(esVocal(letra)){
          if(accion == 'E'){
            /*Si la accion es encriptar, debemos de agregar en la lista despues de la vocal la letra f, seguido de la
            vocal encontrada en minuscula*/
            nuevoMensaje.add('f');
            nuevoMensaje.add(Character.toLowerCase(letra));
          }
          else{
            ignorar = 2; //Si la accion es desencriptar, debemos de ignorar las siguientes 2 letras despues de la vocal
          }
        }
      }
      else{ignorar--;}
    }
    for(int j = 0; j < nuevoMensaje.size(); j++){System.out.print(nuevoMensaje.get(j));}
    System.out.println();
  }
  public static boolean esVocal(char letra){
    //funcion para ve
    char vocales[] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}; //arreglo para las vocales
    for (int i = 0; i < 10; i++){if(letra == vocales[i]){return true;}}
    return false;
  }
}
