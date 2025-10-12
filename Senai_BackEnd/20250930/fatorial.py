numero_a_fatorar = int(input("Digite um número inteiro positivo que deseja saber o resultado do seu Fatorial\n"))
contador = numero_a_fatorar

while contador > 1:
  print(numero_a_fatorar)
  contador -= 1
  numero_a_fatorar *= (contador)
  

print(f"\nO resultado da fatoração é: {numero_a_fatorar}")