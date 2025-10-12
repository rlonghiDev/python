#include <stdio.h>
#include <stdlib.h>


int main(){

float eleitores;
float brancoNulo;
float validos;
float percBrancoNulo;
float percValido;
float parcelaBrancoNulo;
float parcelaValidos;


printf("Digite o número de Eleitores\n");
scanf("%f", &eleitores);
printf("Digite o número de Votos Brancos e Nulos\n");
scanf("%f", &brancoNulo);
printf("Digite o número de Votos Válidos\n");
scanf("%f", &validos);



percBrancoNulo = (brancoNulo/eleitores);
parcelaBrancoNulo = (percBrancoNulo*100);


percValido = (validos/eleitores);
parcelaValidos = (percValido*100);


printf("O percentual de votos Brancos e Nulos é %f \n O percentual de votos Válidos é %f \n.",parcelaBrancoNulo,parcelaValidos);
}



