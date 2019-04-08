//La Tribu Problem K
/*No send*/
#include<bits/stdc++.h>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	long long int n;
	long long int i = 2;
	int div = 2, incremento = 1;
	cin>>n;

	if(n == 1){
		cout<<"1"<<endl;
		return 0;
	}

	if(n%2 != 0){
		i = 3;
		incremento = 2;
	}

	for(;i<=int(sqrt(n));i+=incremento){
		if(n%i == 0) {
			div+=2;
			cout<<i<<endl;
		} 
	}

	cout<<div<<endl;
	return 0;
}
