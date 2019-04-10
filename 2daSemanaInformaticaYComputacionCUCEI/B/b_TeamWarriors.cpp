//Team Warriors Problem B
//No Send
#include <iostream>
#include <string.h>
using namespace std;

int main()
{
	int numFra,lim,cont=0;
	cin>>numFra;
	char frases[numFra][100];
	char faltantes[numFra][100];
	int pangram[numFra];
	for (int i = 0; i < numFra; ++i){
		cin>>frases[i];
	}
	for (int i = 0; i < numFra; ++i){
		for (int j= 0; j < strlen(frases[j]); ++j){
			if (!(frases[i][j]>='a' && frases[i][j]<='z')){
				faltantes[i][j]=frases[i][j];
				pangram[i]=0;
			}
			else{
				pangram[i]=1;
			}
		}
	}
	for (int i = 0; i < numFra; ++i){
		if (pangram[i]==0)
		{
			cout<<"missing "<<faltantes[i]<<endl;
		}
		else{
			cout<<"pangram"<<endl;
		}
	}

	return 0;
}