"""
Carla Borba Brandão Longhi
Enunciado: 
Escreva um programa em Python que peça ao usuário para digitar um número inteiro positivo. O
programa deve gerar a sequência de Fibonacci até o número especificado usando um loop ‘while‘.
"""

limite = int(input("Digite o número limite da sequência Fibonacci: "))

contador = 1
elemento = 0

# lista definida com os números iniciais da sequência Fibonacci 
fibonacci = [1,1]

while contador < limite -1:
    elemento = fibonacci[contador] + fibonacci[contador-1]
    contador += 1
    fibonacci.append(elemento)

print(fibonacci)
