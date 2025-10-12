#Coleta de Dados
numero = float(input("Digite o número que será analisado\n"))

#Processamento / Saída
restoDivisao = numero % 2
if(restoDivisao > 0):
    print("O número é ímpar")
else:
    print("O número é par")
