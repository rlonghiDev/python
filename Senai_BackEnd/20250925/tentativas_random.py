# DESAFIO-RELAMPAGO:
# CRIE UMA VARIAVEL COM UM NUMERO SECRETO DE 1 A 10
# FAÇA UM LOOP FOR ONDE IRA PERGUNTAR PARA O USUARIO
# O PALPITE E DIZER SE ELE ACERTOU OU ERROU
# SE ELE ACERTAR, VOCE PODE INTERROMPER O LOOP COM break
# ELE TERA 6 TENTATIVAS

import random

num1 = random.randint(1, 10)#Seleciona um número inteiro dentro do range 1 a 10 de forma aleatória (sem controle)

tentativa = int(input("Digite um número (inteiro) entre 0 a 10\n"))#Captura a primira tentativa do jogador (fora do looping) já convertido para inteiro

for i in range(5): # range 5 determina o número de tentativas que o jogador terá.
    
    if num1 == tentativa: # Verifica acerto 
        print("Parabéns você acertou o número oculto !!!\n")
        exit(0) # Esse comando encerra a execussão do pŕograma. Se usar break será impressa a última frase, que não faz sentido se o jogador ganhou.
    else:# Se o jogador errou ... 
        tentativa = int(input(f"Não foi dessa vez ... você ainda tem {5 - i} tentativas\n")) # Mensagem para nova tentativa capturando e convertendo para número inteiro

print(f"Não teve jeito .... o número oculto era o {num1}. Começa de novo e boa sorte\n") #Frase para consolar o jogador e revelar o número oculto
