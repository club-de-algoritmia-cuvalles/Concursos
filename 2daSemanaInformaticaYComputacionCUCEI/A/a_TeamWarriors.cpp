//Team Warriors Problem A
//Yes
#include <iostream>
#include <string.h>
using namespace std;

int main()
{
	int numPala,lim,cont=0;
	cin>>numPala;
	char palabras[numPala][100];
	int contador[numPala];

	for (int i = 0; i < numPala; ++i){
		cin>>palabras[i];
	}

	for (int i = 0; i < numPala; i++){
		lim= strlen(palabras[i]);
		for (int j = 0; j < lim; j++){
			if (palabras[i][j]=='a' || palabras[i][j]=='e' || palabras[i][j]=='i' || palabras[i][j]=='o' || palabras[i][j]=='u')
			{
				cont++;
			}
		}
		if (cont>lim/2){
			contador[i]=1;
		} 
		else {
			contador[i]=0;
		}
		cont=0;
	}
	for (int i = 0; i < numPala; ++i){
		cout<<palabras[i]<<endl<<contador[i]<<endl;
	}

	return 0;
}