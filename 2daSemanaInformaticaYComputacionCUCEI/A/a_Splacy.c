//Splacy Problem A//
/*Yes*/
#include <stdio.h>
#include<string.h>
#define T 100

int main()
{
int i,t,j,vocal=0,cons=0;
scanf("%i",&t);
struct dir{
char palabra[21];
}lista_dir[T];
for(i=0;i<t;i++){
scanf("%s",lista_dir[i].palabra);}
for(i=0;i<t;i++){
printf("%s\n",lista_dir[i].palabra);
for(j=0;j<=strlen(lista_dir[i].palabra);j++){	
if(lista_dir[i].palabra[j]=='a'){
vocal++;
}else{
if(lista_dir[i].palabra[j]=='e'){
vocal++;
}else{
if(lista_dir[i].palabra[j]=='i'){
vocal++;
}else{
if(lista_dir[i].palabra[j]=='o'){
vocal++;
}else{
if(lista_dir[i].palabra[j]=='u'){
vocal++;}
else{
cons++;
}}}}}}
if(vocal>cons-1){
printf("1\n");
}else{
if(vocal<=cons-1){
printf("0\n");}
}
vocal=0;
cons=0;}
return 0;
}
