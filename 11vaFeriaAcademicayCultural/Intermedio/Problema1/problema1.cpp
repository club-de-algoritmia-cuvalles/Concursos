/*Problema 1 Cesar Secret
Propuesta de solucion
autor: Efrain Esau Martinez Macias
C++*/
#include <iostream>
#include <string.h>
using namespace std;
int main(int argc, char const *argv[]){
	int clave, n; // enteros para el valor de clave de encriptado y numero de casos
	char mensaje[100]; // arreglo de chars para el mensaje
	cin>>n;
	for(int j = 0; j < n; j++){
		cin>>mensaje;
		clave=3;
		//Desencriptado
		char Aux[150];
		for(int i = 0; i <= strlen(mensaje)-1; i++){
			Aux[i]=mensaje[i]-clave; // le restamos 3 al valor ascii del mensaje encriptado
			if (Aux[i] < 'a') Aux[i]+=26;// si el valor es menor a 'a' le aumentamos 26 para convertirlo en letra
			if (Aux[i] < 'a' or Aux[i] > 'z') Aux[i]=' ';// si no es una letra, significa que es un espacio
		}
		Aux[strlen(mensaje)] = '\0';//agregarmos un fin de linea para evitar imprimir valores basura
		cout<<Aux<<endl;
	}
	return 0;
}
