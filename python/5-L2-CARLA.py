"""
Carla Borba Brandão Longhi
Enunciado: 
Crie um programa em Python que solicite ao usuário uma palavra e, em seguida, verifique se
a palavra é um palı́ndromo (ou seja, se ela pode ser lida da mesma forma de trás para frente).
O programa deve exibir ”A palavra é um palı́ndromo”ou ”A palavra não é um palı́ndromo” de
acordo com o resultado.
"""
palavra = input("Digite a palavra a ser analisada: ")
palavralista = list(palavra)
palavrainvertida = palavralista[::-1]

if palavralista == palavrainvertida:
    print("Essa palavra é um palíndromo")
else:
    print("Essa palavra NÃO é um palíndromo")
