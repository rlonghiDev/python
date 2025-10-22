num = int(input("Digite um número inteiro que deseja descobrir se é primo\n"))
contador = num
while contador > 2:
    contador -= 1
    if (num % contador) == 0:
        print("O número NÃO é primo")
        exit(0)
    
print("O número é primo")
