ano = int(input("Digite o ano a ser analisado:\n "))
if ano < 1582:
    print("Esse ano não pertence ao período do calendário Gregoriano, não pode ser verificado")
    exit(0)

if ano % 4 != 0 and ano % 400 != 0:
    tipoAno = "Ano comum"
elif ano % 100 != 0:
    tipoAno = "Ano bissexto"
else:
    tipoAno = "Ano bissexto"

print(tipoAno)