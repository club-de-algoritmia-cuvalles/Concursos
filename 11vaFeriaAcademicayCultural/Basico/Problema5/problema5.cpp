/*Problema 5 Buscando un caracter
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
C++*/
#include <iostream>
#include<string> //libreria para manejo de la clase string
#include<vector>
using namespace std;

int main() {
 string palabra, caracter_buscado; // string para leer la entrada
 vector<int> indices;
 getline(cin, palabra); // usamos la funcion getline de cin para leer hasta salto de linea
                      // cin por defecto lee hasta un espacio en blanco
 cin >> caracter_buscado;

 for(int i = 0; i < palabra.length(); i++){//for para imprimir la parte superior de la piramide
   /* para comparar strings, utilizamos el metodo compare que proporciona string, el cual devuelve 0 si
    los caracteres son iguales, como argumentos del metodo, indicamos el indice de donde queremos iniciar
    nuestra comparacion, seguido de la longitud de la subcadena a comparar, y por ultimo el string a comparar
    con dicho segmento*/
   if(palabra.compare(i, 1, caracter_buscado) == 0){
     indices.push_back(i);
   }
 }

cout << "Ese caracter se encontro en las posiciones: ";
for(int j = 0; j < indices.size(); j++){cout << indices[j] << " ";}
cout << "\nSe encontraron " << indices.size() << " caracteres con la letra " << caracter_buscado << endl;

 return 0;
}
