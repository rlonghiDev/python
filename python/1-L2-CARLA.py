"""
Carla Borba Brandão Longhi
Enunciado:
Escreva um programa em Python que solicite ao usuário seu nome e exiba uma mensagem de
boas-vindas personalizada, seguindo os critérios abaixo:
(a) O nome deve ser validado para garantir que não contenha números ou caracteres especiais
(apenas letras e espaços são permitidos). Caso contrário, solicite a entrada novamente.
(b) O programa deve exibir a mensagem de boas-vindas com o nome corretamente formatado:
– Apenas a primeira letra de cada nome deve estar em maiúscula (ex.: ”mArIa da sIlvA”deve
ser corrigido para ”Maria Da Silva”).
– O nome deve ser exibido com um espaçamento uniforme, removendo espaços extras.
(c) Além da mensagem padrão "Bem-vindo, <Nome>!", o programa deve incluir uma saudação
que varia conforme o horário do dia:
– Manhã (05h - 12h): "Bom dia, <Nome>!"
– Tarde (12h - 18h): "Boa tarde, <Nome>!"
– Noite (18h - 05h): "Boa noite, <Nome>!"
(d) A mensagem final deve ser exibida com um design estilizado utilizando caracteres especiais
(por exemplo, linhas ou caixas ASCII) para torná-la visualmente agradável.
"""
import datetime
nome = input("Digite seu nome:")
texto = list(nome)

def letras (review_texto):
    for i in review_texto:
        if not i.isalpha() and not i.isspace():
                print("Seu nome contém caracter inválido tente novamente")
                exit()
letras(texto)

termina = nome.title()
hora = datetime.datetime.now().hour

if hora < 12:
     periodo = "Bom dia,"
elif hora >= 12 and hora < 18:
     periodo = "Boa tarde," 
else:
     periodo = "Boa noite,"
     
mensagem = periodo + termina + "!"

def contorno(quadro):
    largura = len(quadro) + 2  # Largura da caixa, considerando o texto e as bordas
    print("+" + "-" * largura + "+")
    print("| " + quadro + " |")
    print("+" + "-" * largura + "+")

contorno(mensagem)
