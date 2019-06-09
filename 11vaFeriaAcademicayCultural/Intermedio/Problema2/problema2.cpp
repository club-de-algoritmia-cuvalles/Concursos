/*Problema 2 Validate an input password
Propuesta de solucion
autor: Luis Arturo De La Garza Navel
C++*/
#include <iostream>
#include<string> //libreria para manejo de la clase string
#include<ctype.h> // libreria para la funciones que verifica si un caracter es digito y mayuscula
using namespace std;

int main() {
 string password; // string para leer la entrada
 bool password_valido = false; // bandera booleana para validar password, inicia en false
 cin>>password;
 //validamos si la cadena no inicie con digito y la longitud este en el limite definido
 if(!isdigit(password[0]) && 5 <= password.length() &&  password.length() <= 13){
   bool numero = false, mayuscula = false;
   for(int i = 0; i < password.length(); i++){
     if(numero && mayuscula){
       //si encontramos un digito dejamos de iterar y validamos el password
       password_valido = true;
       break;
     }
     if(isdigit(password[i])) numero = true;
     if(isupper(password[i])) mayuscula = true;
   }
 }
 if(password_valido){
   cout<<"Valid password"<<endl;
 }
 else{
   cout<<"Invalid password"<<endl;
 }

 return 0;
}
