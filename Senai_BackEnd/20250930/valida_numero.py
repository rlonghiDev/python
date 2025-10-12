import time
while True:

    num = input("Digite um número entre 35 e 40 ou F para terminar\n")

    if num == 'f' or num == 'F':
        print("Programa finalizado pelo usuário")
        exit(0)

    if not num.isdigit():
        print("Digite apenas caracteres numéricos\n")
        time.sleep(3)
        continue

    num = int(num)

    if num < 35 or num > 40:
        print("Número fora do intervalo, tente novamente\n")
        time.sleep(3)
        continue

    else:
        break


print("Número atende os critérios solicitados")