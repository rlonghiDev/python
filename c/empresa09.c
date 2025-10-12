#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(){


//86400s

	char *nomeTrabalhador = (char*)malloc(sizeof(char)*21), *tipoAposentadoria1, *tipoAposentadoria2, *tipoAposentadoria3;
	int anoNascimento, anoInicio, hoje, idade, limiteIdade, limiteTrabalho, limiteIdadeBaixo, limiteTrabalhoBaixo, tempoTrabalho;



	printf("Digite o nome do Trabalhador\n");
	scanf("%s", nomeTrabalhador);
	printf("Digite o ano de Nascimento\n");
	scanf("%i", &anoNascimento);
	printf("Digite o ano em que começou a trabalhar na empresa\n");
	scanf("%i", &anoInicio);
	
	hoje = 2025;
	
	
	tempoTrabalho = 0;
	idade = hoje - anoNascimento;
	tempoTrabalho = hoje - anoInicio;
	limiteIdade = 80;
	limiteTrabalho = 70;
	//tipoAposentadoria1 = "";
	//tipoAposentadoria2 = "";
	//tipoAposentadoria3 = "";
	limiteIdadeBaixo = 70;
	limiteTrabalhoBaixo = 60;
	
	
	
	
	if(idade >= limiteIdade){
	 tipoAposentadoria1 = "Idade";
	}else{
	 tipoAposentadoria1 = "";
	}
	
	if(tempoTrabalho >= limiteTrabalho){
	tipoAposentadoria2 = "Tempo de Trabalho";
	}else{
	tipoAposentadoria2 = " ";
	}
	if(idade >= limiteIdadeBaixo && tempoTrabalho >= limiteTrabalhoBaixo){
	tipoAposentadoria3 = "Idade e tempo de trabalho";
	}else{
	tipoAposentadoria3 = " ";
	}
	
	if(idade >= limiteIdade ||tempoTrabalho >= limiteTrabalho||idade >= limiteIdadeBaixo && tempoTrabalho >= limiteTrabalhoBaixo){
	
	printf ("O colaborador %s pode se aposentar por atender o(s) seguinte(s) critério(s): %s, %s e %s \n",nomeTrabalhador,tipoAposentadoria1,tipoAposentadoria2,tipoAposentadoria3);
	}else{
	printf("O colaborador %s não reune os critérios para aposentadoria \n", nomeTrabalhador);
	}
	
	
	return 0;
	}
	
	
	
	
	
	

	
	
	
	
	
	

