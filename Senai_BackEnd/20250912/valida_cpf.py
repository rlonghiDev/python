#Tratamento na string
cpf = input("Digite seu CPF\n")
cpf = cpf.strip()
cpf = cpf.replace(".","")
cpf = cpf.replace("-","")
cpf = cpf.replace(" ","")
cpf = cpf.replace(",","")
#verifica número de dígitos
if (len(cpf) != 11):
    print("Digite seu CPF corretamente e apenas com números")
    exit(0)

#Verifica dígitos numéricos
if(not cpf.isdigit()):
    print("Numero de CPF inválido, digite novamente de forma correta sem letras")
    exit(0)

#Validação primeiro digito: 
primeiro_digito_verificador = int(cpf[-2]) # Captura penúltimo dígito da string e transforma em número inteiro
cpf_primeiro = cpf[0:9] #Seleciona a parte dos números para a validação do primeiro dígito verificador
lista_cpf = []

#Transforma string em lista de números inteiros
for i in cpf_primeiro:
    lista_cpf.append(int(i))

#Executa a soma da fórmula para validação do primeiro dígito utilizando a lista de inteiros
m = 10
soma_primeiro_digito = 0
for i in lista_cpf:
    soma_primeiro_digito += i * m
    m -= 1

#Fórmula depois da multiplicação e soma dos itens
fator_primeiro_digito = (soma_primeiro_digito * 10) % 11

#Se o fator for 10 então pode considerá-lo zero
if(fator_primeiro_digito == 10):
    fator_primeiro_digito = 0


#Validação do segundo digito

#Captura a última posição da string e converte para inteiro
segundo_digito_verificador = int(cpf[-1])

fator_mult = 11 #Numero inicial para multiplicar os do CPF
cpf_valida_segundo_digito = cpf[0:10] # seleciona uma posição a mais que o do primeiro digito

lista_cpf_segundo_digito = []

#Transforma a string numa lista de números inteiros 
for c in cpf_valida_segundo_digito:
    lista_cpf_segundo_digito.append(int(c))

soma_segundo_digito = 0

#Realiza a multiplicação e soma dos números selecionados do CPF
for i in lista_cpf_segundo_digito:
    soma_segundo_digito += fator_mult * i
    fator_mult -= 1
#Aplica a formula de validação
fator_segundo_digito = (soma_segundo_digito * 10) % 11

#verificação de inválidos conhecidos

#Transforma a string cpf numa lista de inteiros 
cpf_lista_numeros = []
for n in cpf:
    cpf_lista_numeros.append(int(n))

invalido_conhecido1 = [1,1,1,1,1,1,1,1,1,1,1]
invalido_conhecido2 = [2,2,2,2,2,2,2,2,2,2,2]

#Verifica a igualdade da lista com a igualdade dos inválidos conhecidos
if(cpf_lista_numeros == invalido_conhecido1) or (cpf_lista_numeros == invalido_conhecido2):
    print("CPF Inválido")

#Compara os dígitos verificadores com o resultado das fórmulas
elif(fator_primeiro_digito == primeiro_digito_verificador) and (fator_segundo_digito == segundo_digito_verificador):
    print("CPF Válido !!!")
else:
    print("CPF Inválido")