nome = input("Digite seu nome completo\n")
letras = list(nome)
tamanho = len(letras)
contador = 0
somaLetra = 0
espacos = 0

while contador < tamanho:
    testaString = letras[contador]
       
    if testaString.isspace():
        espacos = espacos + 1
    else:
        somaLetra = somaLetra +1

    contador = contador + 1

print("Seu nome possui",somaLetra,"letras\n")
#print("Foram retirados",espacos,"espaços do texto do seu nome")
