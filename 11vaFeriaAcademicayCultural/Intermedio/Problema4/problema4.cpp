/*Problema 4 Without Repetitions
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
C++*/
//Nota: esta solucion no elimina las repeticiones del caracter "¡"
#include <iostream>
#include<string>
#include<vector>
#include<locale>
using namespace std;

int main() {
  string oracion;
  getline(cin, oracion);
  vector<char> nueva_oracion;//vector para la nueva oracion
  bool mayuscula = isupper(oracion[0]); //bandera para verificar si hemos insertado una letra mayuscula
  char caracter_actual = oracion[0], caracter; //variable para comparar las repeticiones contiguas
  nueva_oracion.push_back(caracter_actual);
  for(int i = 1; i < oracion.size(); i++){ //iniciamos del 2do caracter
    caracter = tolower(oracion[i]);
    if(caracter != caracter_actual){
      if(isupper(oracion[i]) && not mayuscula){
        caracter = oracion[i];//cambiamos el caracter a mayuscula para insertarlo en la lista
        mayuscula = true;
      }
      cout << caracter_actual << '\n';
      nueva_oracion.push_back(caracter);
      caracter_actual = caracter;
    }
  }
  for(int j = 0; j < nueva_oracion.size(); j++){cout <<nueva_oracion[j];}
  cout <<endl;
  return 0;
}
