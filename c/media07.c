#include <stdio.h>
#include <stdlib.h>

int main(){

float p1;
float l1;
float p3;
float media;


	printf("Digite a nota P1\n");
	scanf("%f", &p1);
	printf("Digite a nota L1\n");
	scanf("%f", &l1);
	printf("Digite a nota P2\n");
	scanf("%f", &p3);
	
	media = (p1*0.3)+(l1*0.3)+(p3*0.4);
	
	printf("A média final é %f\n", media);
	
}
