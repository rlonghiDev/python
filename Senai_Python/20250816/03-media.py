import random
numeros = []

def geraNumero():
    contador = 0
    while (contador<3):
        aleatorio = random.randint(1,100)
        numeros.append(aleatorio)
        contador = contador +1

geraNumero()

media = sum(numeros)/3

print("Os números gerados são: ", numeros, "\nA média entre eles é", round(media,2))
