/*Problema 4 Palabra Piramide Girada
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
C++*/
#include <iostream>
#include<string> //libreria para manejo de la clase string
using namespace std;

int main() {
 string palabra; // string para leer la entrada
 cin>>palabra;

 for(int i = 1; i < palabra.length(); i++){//for para imprimir la parte superior de la piramide
   cout << palabra.substr(0, i) << endl;
 }

 for(int j = palabra.length(); j > 0; j--){{//for para imprimir la parte inferior de la piramide
   cout << palabra.substr(0, j) << endl;
 }

 return 0;
}
