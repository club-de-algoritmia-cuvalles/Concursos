//La Tribu problem J
//Aceptado(100)
#include<stdio.h>
#include<stdlib.h>
#include<iostream>

using namespace std;

int main(){
    long long int x = 0,y = 0;
    long long int mx = 0;

    cin>>x>>y;
    while(x!=0 && y!=0){

        mx = ((x+y)*(x+y-1))/2;
        if((x+y-1)%2==0) cout<<mx-(y-1)<<endl;
        else cout<<mx-(x-1)<<endl;
        cin>>x>>y;
    }
    return 0;
}
