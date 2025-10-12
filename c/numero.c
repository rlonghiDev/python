#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(){
    
    char numero[100]; //Numero capturado como string para viabilizar a validação do número
    int i = 0; //Para uso no laço for
    int tamanho; //Para uso no laço for

    printf("Digite um número Inteiro válido:\n "); //Solicita o número
   
    scanf("%s",numero); // Lê console
    tamanho = strlen(numero); // Determina tamanho da String lida
    
    //Número negativo é válido
    if(numero[0] =='-'){
        i = 1;
    }
    
    //Validação do numero
   for (i; i < tamanho; i++){
       if (numero[i] == '.'){
           i++;
       }
       if(isdigit(numero[i])== 0){
           printf ("Número digitado inválido. Tente novamente \n");
           return 0;
       }
       
       //"Quebra" da string caracter a caracter para validar se é número.
       //Função isdigit retorna 0 se o caracter analisado não for numérico
    
   }
   
   //Positivo, negativo e zero
   char *tipoNumero;
   int valor = atoi(numero); // transforma string em número inteiro
   
   if(valor > 0){
       tipoNumero = "positivo,";
   }
   if (valor < 0){
       tipoNumero = "negativo,";
   }
   if (valor == 0){
       tipoNumero = "zero,";
   }
   
   
   //Inteiro ou decimal
  char *intDec;
  char *parImpar;

 float valor2 = atof(numero);
 
 float conta;
 conta = valor2 - valor;
 //printf("Valor conta %f \n", conta);
 
 intDec = "";
 parImpar = "";
  
  if (conta == 0){
      intDec = "inteiro";
      int paridade = valor % 2;
      int modParidade = abs(paridade);
      if(modParidade > 0){
          parImpar = " impar";
      }else{
          parImpar = " par";
      }
  }else{
      intDec = "decimal";
  }
  
  printf("O número é %s %s %s \n",tipoNumero,intDec,parImpar);
    
    return 0;
}
