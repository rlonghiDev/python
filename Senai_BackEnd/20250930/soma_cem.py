num = int(input("Digite um número acima de 0 e abaixo de 100\n"))
contador = 0


if num > 100 or num < 0:
    print("Digite um número no intervalo especificado")
    exit(0)

while num < 100:
    num += num + 1
    contador += 1

print(f"Foram necessários {contador} somas sequenciais para chegar no número acima de 100")

