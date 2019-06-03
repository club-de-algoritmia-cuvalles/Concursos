/*Problema 1 Contador Ascendente o Descendente
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
C++*/

#include <iostream>
using namespace std;

int main() {
  /*declaramos las variables de entrada de tipo entero y una variable para indicar
    el tipo de paso (incremental o decremental)*/
  int inferior, superior;

  cin>>inferior;
  cin>>superior;

  /*Comparamos si el limite inferior es menor al superior, de ser asi, nuestra Secuencia
  es ascendente, de lo contrario es descendente, al imprimri omitimos el salto de linea y dejamos
  un espacio despues de imprimir cada numero*/

  if(inferior < superior){ // Secuencia incremental
    for(int i = inferior; i <= superior; i++){
      cout << i << ' ';
    }cout << endl;
  }
  else{ // Secuencia decremental
    for(int j = inferior; j >= superior; j--){
      cout << j << ' ';
    }cout << endl;
  }

  return 0;
}
