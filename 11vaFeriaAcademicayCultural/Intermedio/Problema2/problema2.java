/*Problema 2 Validate an input password
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
Java*/

import java.util.Scanner;

class Problema2{
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    String password = entrada.nextLine();
    boolean passwordValido = false; //bandera booleana para validar password, inicia en false
    //validamos que la cadena no inicie con un numero
    boolean iniciaConDigito = !(Character.isDigit(password.charAt(0)));
    if(iniciaConDigito && 5 <= password.length() && 13 >= password.length()){
      boolean numero = false, mayuscula = false;
      for(int i = 0; i < password.length(); i++){
        char elemento = password.charAt(i); // accedemos al caracter en el indice i
        if(numero && mayuscula){
          //si encontramos un digito dejamos de iterar y validamos el password
          passwordValido = true;
          break;
        }
        if(Character.isDigit(elemento)) numero = true;
        if(Character.isUpperCase(elemento)) mayuscula = true;
      }
    }
    if(passwordValido){
      System.out.println("Valid password");
    }
    else{
      System.out.println("Invalid password");
    }
  }
}
