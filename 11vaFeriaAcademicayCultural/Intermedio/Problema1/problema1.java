/*Problema 1 Cesar Secret
Propuesta de solucion
autor: Efrain Esau Martinez Macias
Java*/
import java.util.Scanner;

class Problema1{
  public static void main(String[] args) {
    int clave = 3;
    Scanner entrada = new Scanner(System.in);
    int n = entrada.nextInt();
    entrada.nextLine();
    for(int i = 0; i < n; i++){
      String mensaje = entrada.nextLine();
      char [] Aux = new char[150];
      for(int j = 0; j < mensaje.length(); j++){
        //obtenemos el valor ascii del caracter y le restamos la clave oara desencriptar
        int valor = mensaje.codePointAt(j) - clave;
        Aux[j] = (char)valor;//convertimos el valor ascii a char
        if (Aux[j] < 'a') Aux[j]+=26;// si el valor es menor a 'a' le aumentamos 26 para convertirlo en letra
    		if (Aux[j] < 'a' || Aux[j] > 'z') Aux[j]=' ';// si no es una letra, significa que es un espacio
      }
      Aux[mensaje.length()] = '\0';//agregarmos un fin de linea para evitar imprimir valores basura
      System.out.println(Aux);
    }
  }
}
