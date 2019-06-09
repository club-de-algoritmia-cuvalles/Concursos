/*Problema 5 Baker Palindromes
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
C++*/
import java.util.Scanner;

class Problema5{
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    int t = entrada.nextInt();
    int n;
    boolean par, pdr;
    String palabra;
    for(int i = 0; i < t; i++){
      palabra = entrada.next();
      n = entrada.nextInt();
      par = esPalindromo(palabra);
      palabra = rotate(palabra, n);
      pdr = esPalindromo(palabra);
      if(par) {
        if(pdr) System.out.println("Baker Palindrome");
        else System.out.println("Palindrome");
      }
      else{
        if(pdr) System.out.println("Possible Baker Palindrome");
        else System.out.println("No Baker Palindrome");
      }
    }
  }
  public static boolean esPalindromo(String palabra){
    for(int i = 0, j = palabra.length()-1; i<palabra.length(); i++, j--){
      if(palabra.charAt(i) != palabra.charAt(j)){
        return false;
      }
    }
    return true;
  }

  public static String rotate(String palabra, int n){
    char aux, temp;
    char cadenaAux[] = palabra.toCharArray();
    for(int i = 0; i < n; i++){
      aux = cadenaAux[palabra.length() - 1];
      for(int j = palabra.length()-1; j > 0; j--){cadenaAux[j] = cadenaAux[j-1];}
      cadenaAux[0] = aux;
    }
    return String.valueOf(cadenaAux);
  }
}
