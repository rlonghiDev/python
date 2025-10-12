"""
Carla Borba Brandão Longhi
Enunciado: 
Os números primos possuem várias aplicações dentro da Computação, por exemplo na Cripto-
grafia. Um número primo é aquele que é divisı́vel apenas por um e por ele mesmo. Faça um
programa em Python que peça um número inteiro e determine se ele é ou não um número primo.
"""
testenum = int(input("Digite o número e verifique se ele é primo: "))

contador = testenum -1

while contador > 1:
    if (testenum % contador) == 0:
        print("Esse número NÃO é primo")
        print("Esse número tem divisão exata por: ", contador)
        exit()
    contador -= 1
    
print("Esse número é primo")
