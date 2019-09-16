//La Tribu Problem C
//Yes
#include<bits/stdc++.h>
using namespace std;

int main(){
	int n, k, mod, res;
	bool a;
	long pin;

	cin>>n;
	for(int i=0; i<n; i++){
		cin>>k;
		pin=10;
		mod = int((k-1)/10);
        res = (k-1)%10;
        for(int z=0;z<mod;z++){
        	pin = pin*486784380;
        	pin%=1000000007;
        }
		for(int j=0;j<res;j++){
		 	pin = (pin*9);
		 	pin%=1000000007;
		}
		cout<<pin<<endl;
	}
	return 0;
}
