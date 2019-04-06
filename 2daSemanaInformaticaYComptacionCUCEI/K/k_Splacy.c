/*Splacy Problem K */
/*Run Time Error*/
#include <stdio.h>
int main(){
long long int i=1,num;
int band=0;
scanf("%lli",&num);
for(i=1;i<=num/2;i++){
if(num%2!=0)
	break;
if(num%i==0)
band++;
}
band++;
printf("%i",band);
return 0;
}
