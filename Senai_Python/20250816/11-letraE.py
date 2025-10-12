frase = input("Digite uma frase\n")
letrasDaFrase = list(frase)
tamanho = len(letrasDaFrase)
contador = 0
letrase = 0

while contador < tamanho:
    if letrasDaFrase[contador] == 'e' or letrasDaFrase[contador] =='E':
        letrase = letrase + 1
    
    contador = contador + 1


print('Existem',letrase,'letras "e" ou "E" na frase digitada')