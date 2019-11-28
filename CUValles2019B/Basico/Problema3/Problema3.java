/*
Problema 3: Separar frase
Autor de la solucion: AlbertAvile.
Java 8
Descripcion del problema:Recibiremos una frase, la cual puede contener cualquier
tipo de caracter, y debemos de separar los numeros de los demas caracteres,
y los numeros deben ser sumados
Entrada: Ae78YuPo5?8&40
Salida:
Cadena numérica 785840
Cadena no numérica: AeYuPo?&
la suma de la cadena numérica es: 32
Explicacion: Debemos de tomar toda la frase, usando 2 arreglos, debemos de mandar
en una de ellas los numeros, y en el otro los demas caracteres; se debera mostrar
el contenido de ambas listas, y convertir los caracteres numericos en int para
ser sumados
*/

import java.util.Scanner;
import java.util.ArrayList;

public class Problema3{
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    String cadena = entrada.nextLine();

    ArrayList<Character> numeros = new ArrayList<Character>();
    ArrayList<Character> caracteres = new ArrayList<Character>();
    int suma = 0;

    for(int i = 0; i < cadena.length(); i++){
      if(Character.isDigit(cadena.charAt(i))){
        numeros.add(cadena.charAt(i));
        suma += Integer.parseInt(""+cadena.charAt(i));
      }
      else{
        caracteres.add(cadena.charAt(i));
      }
    }
    System.out.print("Cadena num\u00e9rica ");
    for(int j = 0; j < numeros.size(); j++){System.out.print(numeros.get(j));}
    System.out.println();

    System.out.print("Cadena no num\u00e9rica: ");
    for(int j = 0; j < caracteres.size(); j++){System.out.print(caracteres.get(j));}
    System.out.println();

    System.out.println("la suma de la cadena num\u00e9rica es: "+suma);
  }
}