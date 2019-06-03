 /*Problema 3 Validando Password
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
C++*/
#include <iostream>
#include<string> //libreria para manejo de la clase string
#include<ctype.h> // libreria para la funcion que verifica si un caracter es digito
using namespace std;

int main() {
  string password; // string para leer la entrada
  bool password_valido = false; // bandera booleana para validar password, inicia en false
  cin>>password;
  //validamos si la cadena no inicie con digito y la longitud este en el limite definido
  if(!isdigit(password[0]) && 5 <= password.length() &&  password.length() <= 13){
    for(int i = 1; i < password.length(); i++){
      if(isdigit(password[i])){
        //si encontramos un digito dejamos de iterar y validamos el password
        password_valido = true;
        break;
      }
    }
  if(password_valido){
    cout<<"Password valido"<<endl;
  }
  else{
    cout<<"Password invalido"<<endl;
  }

  return 0;
}
