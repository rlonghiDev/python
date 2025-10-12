#include <stdio.h>
#include <string.h>



void conta_vogal(){
		char nome[15];
			int tamanho = 0, vogal = 0;
			printf("\n Digite uma palavra: \n");
			scanf("%s",nome);
			tamanho = strlen(nome);
			
			for (int i = 0; i < tamanho; i++){
			
			if(nome[i] == 'a' ||
			nome[i] == 'A' ||
			nome[i] == 'e' ||
			nome[i] == 'E' ||
			nome[i] == 'i' ||
			nome[i] == 'I' ||
			nome[i] == 'o' ||
			nome[i] == 'O' ||
			nome[i] == 'u' ||
			nome[i] == 'U' ){
				vogal++;
			 	}
			}
			printf ("\n O nome %s tem %d vogal(is)\n", nome, vogal);
			}
			
			
int main(){

	conta_vogal();
		
return 0;			
		
}			
			

