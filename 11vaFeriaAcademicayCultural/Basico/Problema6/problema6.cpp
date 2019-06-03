/*Problema 6 Lenguaje de la F
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
C++*/
#include <iostream>
#include<string> //libreria para manejo de la clase string
#include<vector>
#include <ctype.h>
using namespace std;
bool es_vocal(char letra){
  char vocales[] =  {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}; //array de strings para buscar las vocales
  for(int i = 0; i < 10; i++){
    if(vocales[i] == letra){// comparamos la vocal con la letra del vector en la posicion i
      return true;
    }
  }
  return false;
}
int main() {
 string accion, mensaje; // string para leer la entrada
 vector<char> nuevo_mensaje;
 int ignorar = 0;
 cin.ignore();
 getline(cin, accion);
 getline(cin, mensaje); // usamos la funcion getline de cin para leer hasta salto de linea
                      // cin por defecto lee hasta un espacio en blanco
 for(int i = 0; i < mensaje.length(); i++){//for para imprimir la parte superior de la piramide
   if(ignorar == 0){
      nuevo_mensaje.push_back(mensaje[i]);
      if(es_vocal(mensaje[i])){
        if(accion.compare("E")==0){
          nuevo_mensaje.push_back('f');
          nuevo_mensaje.push_back(tolower(mensaje[i]));
        }
        else{ignorar = 2;}
      }
   }
   else{ignorar--;}
 }
 for(int j = 0; j < nuevo_mensaje.size(); j++){cout << nuevo_mensaje[j];}
 cout << endl;
 return 0;
}
