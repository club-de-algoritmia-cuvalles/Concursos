/*Problema 3 Validando Password
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
Java*/

import java.util.Scanner;

class Problema3{
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    String password = entrada.nextLine();
    boolean passwordValido = false; //bandera booleana para validar password, inicia en false
    //validamos que la cadena no inicie con un numero
    boolean iniciaConDigito = !(Character.isDigit(password.charAt(0)));
    if(iniciaConDigito && 5 <= password.length() && 13 >= password.length()){
      for(int i = 1; i < password.length(); i++){
        char elemento = password.charAt(i); // accedemos al caracter en el indice i
        if(Character.isDigit(elemento)){
          //si encontramos un digito dejamos de iterar y validamos el password
          passwordValido = true;
          break;
        }
      }
    }
    if(passwordValido){
      System.out.println("Password valido");
    }
    else{
      System.out.println("Password invalido");
    }
  }
}
