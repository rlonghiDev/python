# Aluno: Ronaldo Longhi -- Atividade: Lista de exercício Tema: "for" ministrada em 06/09/2025

#1. Crie uma estrutura de repetição que percorre a string o seu nome, exibindo 
#em tela letra por letra desse nome

# nome = 'Ronaldo'
# for letra in nome:
#     print(letra)


# Crie um programa que lê um valor de início e um valor de fim, exibindo em 
# tela a contagem dos números dentro desse intervalo.


#solucao
# inicio = int(input("insira o valor de inicio\n"))
# fim = int(input("insira o valor de fim\n"))
# contagem = 0

# for numero in range(inicio,fim):
#     contagem += 1

# print(contagem)

# 3. Crie um programa que realiza a contagem de 0 a 20, exibindo apenas os 
# números pares:


# for i in range(0,21):
#     if (i % 2) == 0:
#         print(i)

# 4 - Crie um programa que realiza a Progressão Aritmética de 20 elementos, 
# com primeiro termo e razão definidos pelo usuário

# primeiroTermo = int(input('Digite o primeiro termo da PA\n'))
# razao = int(input('Digite a razão da PA\n'))
# print("\n")
# for etapa in range(0,20):
#     print (primeiroTermo)
#     primeiroTermo += razao


# 5. Crie um programa que exibe em tela a tabuada de um determinado número 
# fornecido pelo usuário:

# tabuada = int(input("Digite um número entre 1 e 10\n"))
# multiplicador = 0
# resultado = 0

# for etapa in range(0,11):
#     print(multiplicador,"x",tabuada,"=",resultado)
#     multiplicador += 1
#     resultado = multiplicador * tabuada
# print("\n")


#6. Crie um programa que realiza a contagem regressiva de 20 segundos:

# import time
# contagem = 20
# for t in range (0,21):
#     print(contagem)
#     contagem -= 1
#     time.sleep(1)
# print("acabou")

# 7. Crie um programa que realiza a contagem de 1 até 100, usando apenas de 
# números ímpares, ao final do processo exiba em tela quantos números 
# ímpares foram encontrados nesse intervalo, assim como a soma dos 
# mesmos:

# contagem = 0 
# soma = 0

# for numero in range (0,100):
#     if (numero % 2) != 0:
#         contagem += 1
#         soma += numero
# print("\n A quantidade de números ímpares entre 0 até 100 é: ", contagem,"\n","A soma de todos os números ímpares é: ", soma,"\n")

# 8. Crie um programa que pede ao usuário que o mesmo digite um número 
# qualquer, em seguida retorne se esse número é primo ou não, caso não, 
# retorne também quantas vezes esse número é divisível

# numero = int(input("Digite um número para verificar se é primo\n"))
# divisao = 0
# contagem = 0

# for primo in range(numero,0,-1):
#     if(numero % primo) == 0:
#         divisao += 1
        

# if (divisao <= 2):
#     print("Esse número é primo")
# else:
#     print("Esse número NÃO é primo, teve divisão exata por", divisao,"vezes\n")




