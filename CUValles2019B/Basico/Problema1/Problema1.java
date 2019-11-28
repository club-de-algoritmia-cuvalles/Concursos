/*
Problema 1: Repetir cadena numerica
Autor de la solucion: AlbertAvile.
Java 8
Descripcion del problema:
Recibiremos una cadena de numeros de cualquier longitud
y deberemos de imprimir el digito n + 1 veces si se encuentra
en una posicion par (0 es par), y n - 1 veces si se encuentra
en una posicion impar.
Ejemplo:
Entrada: 7245314
Salida:
88888888
1
55555
4444
4444
0
55555
Explicacion: debemos de guardar el numero como una cadena para poder recorrerla;
las posiciones para el ejemplo anterior seria el siguiente
============================================
SIMBOLOGIA: P = par, I = impar            ||
============================================
paridad : P || I || P || I || P || I || P ||
============================================
posicion: 0 || 1 || 2 || 3 || 4 || 5 || 6 ||
============================================
numero  : 7 || 2 || 4 || 5 || 3 || 1 || 4 ||
============================================
Para el caso de tener una posicion par nosotros vamos a sumar uno al numero.
Ejemplo:
posicion: 0, numero: 7
numero = 7 + 1 = 8
Y como salida debemos de imprimir 8 veces el numero 8 de la siguiente manera:
88888888
Para el caso de tener una posicion impar nosotros vamos a restar uno al numero.
Ejemplo:
posicion: 1, numero: 2
numero = 2 - 1 = 1
Y como salida debemos de imprimir 1 vez el numero 1 de la siguiente manera:
1
*/
import java.util.Scanner;

public class Problema1{
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    String cadena = entrada.nextLine();
    
    for(int i = 0; i < cadena.length(); i++){
      int elemento = Integer.parseInt(""+cadena.charAt(i)); // accedemos al caracter en el indice i y lo covertimos a entero
      
      if(i%2 == 1){//si el indice es impar
        elemento -= 1;//restamos 1 al elemento
      }
      else{//si el indice es par 
        elemento += 1;//sumamos 1 al elemento
      }

      for (int j = 0; j < elemento; j++) {//imprimimos el elemento la cantidad de veces que su valor
          System.out.print(elemento);
      }
      if(elemento == 0){//si el elemento fue 0 solamente imprimimos un 0
        System.out.print(elemento);
      }
      System.out.println();//agregamos el salto de linea
      
    }
  }
}
