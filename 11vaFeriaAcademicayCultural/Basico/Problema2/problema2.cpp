/*Problema 2 Solo numeros
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
C++*/

#include <iostream>
#include<string> //libreria para manejo de la clase string
#include<ctype.h> // libreria para la funcion que verifica si un caracter es digito
using namespace std;

int main() {
  string entrada; // string para leer la entrada
  int acumulador = 0; // int para acumular los caracteres que son digitos

  cin>>entrada;

  for(int i = 0; i < entrada.length(); i++){
    if(isdigit(entrada[i])){
      /* le restamos a caracter 48, que es el del cero (primer numero) de Ascii*/
      acumulador += entrada[i] - 48;
    }
  }
  cout << acumulador << endl;

  return 0;
}
