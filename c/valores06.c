#include <stdio.h>
#include <stdlib.h>

int main(){

int v1;
int v2;
int v3;


	printf("Digite o primeiro valor\n");
	scanf("%i", &v1);
	printf("Digite o segundo valor\n");
	scanf("%i", &v2);
	printf("Digite o terceiro valor\n");
	scanf("%i", &v3);
	
	
int p1;
int p2;
int p3;

	//Menor número(p1)
	if(v1<v2){
	p1 = v1;
	}
	if(v2<v1){
	p1 = v2;
	}
	if(v3<p1){
	p1 = v3;
	}
	
	//Maior número(p3)
	
	if(v1>v2){
	p3 = v1;
	}
	if(v2>v1){
	p3 = v2;
	}
	if(v3 > p3){
	p3 = v3;
	}
	
	//Número intermediario(p2)
	
	if(v1 == p1 && v2 == p3){
	p2 = v3;
	}
	
	if(v2 == p1 && v3 == p3){
	p2 = v1;
	}
	
	if(v3 == p1 && v1 == p3){
	p2 = v2;
	}
	
	printf("%d, %d, %d\n",p1,p2,p3);
	
	
}
	

