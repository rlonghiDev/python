#Coleta de Dados
num1 = float(input("Digite o primeiro número\n"))
num2 = float(input("Digite o segundo número\n"))

#Processamento / Saída
if (num1 > num2):
    print("O maior maior número é o: ", num1)
    exit()

if(num1 == num2):
    print("Os números são iguais")
else:
    print("o maior número é o: ", num2)
