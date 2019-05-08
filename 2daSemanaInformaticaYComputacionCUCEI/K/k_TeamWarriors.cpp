//Team Warriows Problem K
/*?*/
#include <iostream>
#include <math.h>
using namespace std;

int main(){
	int dividendo;
	cin>>dividendo;
	int mitad = dividendo/2;
	int contador = 0;
	for (int i=1; i<=sqrt(dividendo); i++){
		if (dividendo%i == 0){
			contador++;
			if(i*2<=mitad){
				contador++;
			}
		}
	}
	cout<<contador<<endl;
	return 0;
}
