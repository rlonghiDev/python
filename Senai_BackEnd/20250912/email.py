#Exercício 3 (e-mail)
#Solicita ao usuário o endereço de email
email = input("Digite seu e-mail\n")

#caputa tamanho e posição
tamanho = (len(email)-1)
posicao_arroba = email.find("@")

#verifica se existe "@" e se existe nome do servidor.
#Se não houver "@" na string email a variável posicao_arroba assume -1
#Para o caso da variável posicao_arroba ser igual ao tamanho não foi digitado o nome do servidor.
#Qualquer uma das duas hipóteses, se válida, o endereço digitado é caracterizado como inválido
if(posicao_arroba == tamanho) or (posicao_arroba < 0):
    print("Email inválido, digite novamente")
    exit(0)

#Captura o nome do servidor (usa fatiamento da string a partir do arroba)
servidor_email = email[(posicao_arroba + 1):] #Tudo depois do arroba (exceto o arroba)

#verificação do nome do servidor de e-mail, apenas a existência de 1 ponto
#print(servidor_email)

ponto = servidor_email.find(".")
#Caso não exista o caractere "." na string contida em servidor_email o retorno será -1
#O endereço digitado se torna inválido
if(ponto < 0):
    print("E-mail inválido, digite novamente")
else:
    print(email,"é um e-mail válido")

#Esse algorítmo apenas verifica itens básicos de um e-mail
#Não consegue avaliar sua real validade porque há erros de
#digitação que não podem ser controlados.
