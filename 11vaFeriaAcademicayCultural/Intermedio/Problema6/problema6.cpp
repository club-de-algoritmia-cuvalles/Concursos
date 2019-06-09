/*Problema 6 Mateo Towers
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
C++*/
#include <iostream>
#include <cctype>
#include<string>
#include <vector>
using namespace std;

int buscar_bloque(vector<char> &torres, char torre){//funcion para comprobar si una torre se encuentra en el vector
  for(int i = 0; i < torres.size(); i++){
    if(torres[i] == torre) return i;//retorna la posicion donde se encontro la torre
  }
  return -1;//retornar -1 si no se encuentra el bloque
}

int main(){
  int n, bloque;
  cin >> n;
  string bloques;
  cin >> bloques;
  vector<char> torres;
  vector<int> cantidad_torres;
  for(int i = 0; i < n; i++){
    bloque = buscar_bloque(torres, toupper(bloques[i]));
    if(isupper(bloques[i])){//si el bloque es una letra maysucula
      if(bloque != -1){
        cantidad_torres[bloque]++;//si se encontro el bloque se incrementa en uno la cantidad
      }
      else{//si el bloque no fue encontrado, lo agragamos al vector de torres y al de cantidad lo inicamos en 1
        torres.push_back(bloques[i]);
        cantidad_torres.push_back(1);
      }
    }
    else{
      if(bloque != -1){
        cantidad_torres[bloque]--;//si se encuentra el bloque se disminuye en uno la torre
        if(cantidad_torres[bloque] == 0){//si quedan 0 bloques, retiramos la tore y su respectivo contador
          torres.erase(torres.begin() + bloque);
          cantidad_torres.erase(cantidad_torres.begin() + bloque);
        }
      }
    }
  }
  for(int j = 0; j < torres.size(); j++){cout << torres[j] << cantidad_torres[j] <<endl;}
  return 0;
}
