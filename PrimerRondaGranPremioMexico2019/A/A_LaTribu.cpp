//La Tribu Problem A
//No Time Limit Exceeded
//#include <bits/c++.h>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, a, res, suma = 0;
    vector<int> alumnos;

    cin>>n;
    for(int x = 0; x<n; x++){
        cin>>a;
        alumnos.push_back(a);
    }

    for(int i = 0; i<n; i++){
        for(int j = i+1; j<n; j++){
            res = alumnos[j] - alumnos[i];
            if(res<-1 or res>1){
                suma += res;
            }
        }
    }

    cout<<suma<<endl;

    return 0;
}
