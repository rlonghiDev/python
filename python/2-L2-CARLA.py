"""
Carla Borba Brandão Longhi
Enunciado: 
Crie um programa em Python que peça ao usuário para digitar três números inteiros. O programa
deve comparar os números e exibir o maior deles.
"""

num1 = int(input("Informe o primeiro número inteiro: "))
num2 = int(input("Informe o segundo número inteiro: "))
num3 = int(input("Informe o terceiro número inteiro: "))

if num1 > num2 and num1 > num3:
  print(f"O maior número é {num1}.")
elif num2 > num1 and num2 > num3:
  print(f"O maior número é {num2}.")
elif num1 == num2 == num3:
  print(f"Os três números são iguais.")
else:
  print(f"O maior número é {num3}.")

