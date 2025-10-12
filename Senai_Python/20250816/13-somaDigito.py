numero = input("Digite até 4 números\n")
listaNumero = list(numero)
contador = 0 
tamanho = len(listaNumero)
soma = 0 

while contador < tamanho:
    soma = soma + int(listaNumero[contador])
    contador += 1



print("A soma dos dígitos é:", soma)