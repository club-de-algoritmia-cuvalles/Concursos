/*
Problema 2: Iniciales en Minusculas
Autor de la solucion: AlbertAvile.
Java 8
Descripcion del problema:Recibiremos una frase, la cual las iniciales de
cada palabra deben ser convertidas en minusculas, y el resto de la palabra en
mayusculas
Entrada: The dArK SidE oF tHe MoOn
Salida: tHE dARK sIDE oF tHE mOON
Explicacion: Debemos de tomar toda la frase (incluyendo espacios en blanco), e
ir cambiando a minusculas a las letras que inician la palabra, esto se puede hacer
buscando los espacios en blanco, una vez que encontramos la inicial, convertimos
a toda letra a mayusculas, esto hasta encontrar otro espacio y repetimos la accion
para toda la frase.
*/

import java.util.Scanner;

public class Problema2{
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    String cadena = entrada.nextLine();//leemos la cadena

    Boolean inicial = true;//creamos una variable bandera para indicar si la letra es la inicial de cada palabra
    
    for(int i = 0; i < cadena.length(); i++){
      if(inicial){//si la letra es la inicial la convertimos a minuscula
        System.out.print((""+cadena.charAt(i)).toLowerCase());
        inicial = false;//igualamos a false la bandera ya que las siguientes no seran la inicial
      }
      else{
        System.out.print((""+cadena.charAt(i)).toUpperCase());//convertimos las letras no iniciales a mayusculas

        if(Character.isSpace(cadena.charAt(i))){//si encontramos un espacio regresamos la variable a true
            inicial = true;
        }
      }
      
    }
  }
}