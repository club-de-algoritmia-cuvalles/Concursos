/*Problema 6 Mateo Towers
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
Java*/
import java.util.Scanner;
import java.util.ArrayList;

class Problema6{
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    int n = entrada.nextInt();
    entrada.nextLine();
    int bloque, valor;
    String bloques = entrada.nextLine();
    ArrayList<Character> torres = new ArrayList<Character>();
    ArrayList<Integer> cantidadTorres = new ArrayList<Integer>();
    for(int i = 0; i < n; i++){
      bloque = buscar_bloque(torres, Character.toUpperCase(bloques.charAt(i)));
      if(Character.isUpperCase(bloques.charAt(i))){//si el bloque es una letra maysucula
        if(bloque != -1) cantidadTorres.set(bloque, cantidadTorres.get(bloque) + 1);//si se encontro el bloque se incrementa en uno la cantidad
        else{//si el bloque no fue encontrado, lo agragamos al vector de torres y al de cantidad lo inicamos en 1
          torres.add(bloques.charAt(i));
          cantidadTorres.add(1);
        }
      }
      else{
        if(bloque != -1){
          cantidadTorres.set(bloque, cantidadTorres.get(bloque) - 1);//si se encuentra el bloque se disminuye en uno la torre
          if(cantidadTorres.get(bloque) == 0){//si quedan 0 bloques, retiramos la tore y su respectivo contador
            torres.remove(bloque);
            cantidadTorres.remove(bloque);
          }
        }
      }
    }
    for(int j = 0; j < torres.size(); j++){System.out.print(torres.get(j));System.out.println(cantidadTorres.get(j));}
  }
  public static int buscar_bloque(ArrayList<Character> torres, char torre){//funcion para comprobar si una torre se encuentra en el vector
    for(int i = 0; i < torres.size(); i++){
      if(torres.get(i) == torre) return i;//retorna la posicion donde se encontro la torre
    }
    return -1;//retornar -1 si no se encuentra el bloque
  }
}
