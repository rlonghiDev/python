"""
Carla Borba Brandão Longhi
Enunciado: 
Faça um programa em Python que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5! =120.
"""
fatoracao = int(input("Digite o número a ser fatorado: "))
contador = fatoracao
num = fatoracao -1 
multiplica = fatoracao

while contador > 2:
    fatoracao = fatoracao * num
    num -= 1
    contador -= 1

print(multiplica,"! = ",fatoracao)
