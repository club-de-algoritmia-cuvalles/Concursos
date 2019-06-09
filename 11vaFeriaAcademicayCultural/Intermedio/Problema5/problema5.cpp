/*Problema 5 Baker Palindromes
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
C++*/
#include <iostream>
#include <string>
using namespace std;

bool es_palindromo(string palabra){
  for(int i = 0, j = palabra.size()-1; i<palabra.size(); i++, j--){
    if(palabra[i]!=palabra[j]){
      return false;
    }
  }
  return true;
}

void rotate(string &palabra, int n){
  char aux;
  for(int i = 0; i < n; i++){
    aux = palabra[palabra.size() - 1];
    for(int j = palabra.size()-1; j > 0; j--){swap(palabra[j], palabra[j-1]);}
    palabra[0] = aux;
  }
}

int main() {
  int t, n;
  cin >> t;
  bool par, pdr;
  string palabra;
  for(int i = 0; i < t; i++){
    cin >> palabra;
    cin >> n;
    par = es_palindromo(palabra);
    rotate(palabra, n);
    pdr = es_palindromo(palabra);
    if(par) {
      if(pdr) cout << "Baker Palindrome" << endl;
      else cout << "Palindrome" << endl;
    }
    else{
      if(pdr) cout << "Possible Baker Palindrome" << endl;
      else cout << "No Baker Palindrome" << endl;
    }
  }
  return 0;
}
