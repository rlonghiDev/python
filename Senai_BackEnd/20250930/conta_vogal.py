palavra = input("Digite uma palavra ou frase\n")

contador = 0

for l in palavra:
    
    if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
        contador += 1
    
    if l == 'A' or l == 'E' or l == 'I' or l == 'O' or l == 'U':
        contador += 1
        
print("O número de vogais encontradas é:",contador)