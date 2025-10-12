numero = float(input("Digite um número\n"))
teste1 = numero%3
teste2 = numero%5
if teste1 == 0 and teste2 == 0:
    print("O número pode ser dividido por 3 e por 5 ao mesmo tempo")
else:
    print("Esse número não pode ser dividido por 3 e 5 ao mesmo tempo")