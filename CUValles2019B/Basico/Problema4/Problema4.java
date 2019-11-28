/*
Problema 4: Palabra mariposa
Autor de la solucion: AlbertAvile.
Java 8
Descripcion del problema: Dado una palabra mostrar en pantalla la figura que
simula una mariposa como se muestra en la salida
Entrada: Tinieblas
Salida:
T                T
Ti              iT
Tin            niT
Tini          iniT
Tinie        einiT
Tinieb      beiniT
Tiniebl    lbeiniT
Tiniebla  albeiniT
TinieblassalbeiniT
TinieblassalbeiniT
Tiniebla  albeiniT
Tiniebl    lbeiniT
Tinieb      beiniT
Tinie        einiT
Tini          iniT
Tin            niT
Ti              iT
T                T
Explicacion: Si observamos la figura, veremos que la figura se forma con la
aparicion de una de las letras de la palabra, para el primer renglon, tenemos
a la letra 'T', para el segundo la palabra 'Ti', y este proceso se repite por
la longitud de la palabra, y este proceso a su vez se repite de manera inversa
para formar la parte inferior. Para formar cada linea podemos considerar lo
siguiente:
1ra mitad
1/2 linea = palabra[0 -> i] + (" " * i)
Indicamos que tomaremos las letras de la posicion 0 hasta i, donde i es el renglon
a imprimir, y le vamos a sumar la cantidad de espacios para completar la
longitud de la palabra. El resultado obtenido debe de reflejarse del otro resultado
por lo que la linea seria:
linea = 1/2 linea + invertir(linea)
Esto aplica tanto para la parte superior y para la inferior, en esta ultima, recorreremos
los valores del renglon empezando desde la longitud de la palabra hasta 1.
*/

import java.util.Scanner;

public class Problema4{
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    String cadena = entrada.nextLine();
    
    for(int i = 0; i < cadena.length(); i++){
      System.out.print(cadena.substring(0,i+1));
      for(int j = 0; j < (cadena.length()-i-1)*2; j++){
        System.out.print(" ");
      }
      System.out.println(new StringBuilder(cadena.substring(0,i+1)).reverse().toString());
    }

    for(int i = cadena.length(); i > 0; i--){
      System.out.print(cadena.substring(0,i));
      for(int j = 0; j < (cadena.length()-i)*2; j++){
        System.out.print(" ");
      }
      System.out.println(new StringBuilder(cadena.substring(0,i)).reverse().toString());
    }
  }
}