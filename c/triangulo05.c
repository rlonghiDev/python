#include <stdio.h>
#include <stdlib.h>

int main(){
//Triângulo Isóceles -- dois lados iguais 
//Triângulo Equilátero -- todos os lados iguais 
//Triângulo Escaleno -- todos os lados diferentes 

int lado1;
int lado2;
int lado3;



	printf("Digite a medida do primeiro lado do triângulo\n");
	scanf("%i", &lado1);
	printf("Digite a medida do segundo lado do triângulo\n");
	scanf("%i", &lado2);
	printf("Digite a medida do terceiro lado do triângulo\n");
	scanf("%i", &lado3);
	
	
		if(lado1 == lado2 && lado1 == lado3){
		printf ("\nTriângulo Equilátero\n");
		return 0;
		}
		
		if(lado1 == lado2 || lado2 == lado3 || lado1 == lado3){
		printf ("\nTriângulo Isósceles\n");
		return 0;
		}
		
		if(lado1 != lado2 && lado2 != lado3 && lado1 != lado3){
		printf ("\nTriângulo Escaleno\n");
		return 0;
		}
}
		
		
	
	
