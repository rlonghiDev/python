#seu código aqui
#Cria lista bidimensional(1 linha e uma coluna)
import time
hotel = [[]]

#Cria variável responsável por indicar o quarto do hóspede no hotel
insercao_quarto = 0

while True:
    #Recebe a quantidade de hospedes que ficarão no quarto e ofere o escape do looping de cadastro
    qde_hospedes = int(input("Informe a quantidade de hospedes que ficarão no mesmo quarto, para encerrar digite 0 (zero)\n"))

    #Escape do looping de cadastro
    if qde_hospedes == 0:
        break

    #Máximo de 4 hóspedes por quarto
    elif qde_hospedes > 4:
      print("Número máximo de hóspedes por quarto é 4.\n")
      time.sleep(3)
      continue

    #Cria novo quarto depois que a primeira alocação foi feita no "quarto" zero.
    if insercao_quarto != 0:
        #Cria quarto
        hotel.append([''])
        #Apaga posição vazia do quarto(sujeira)
        hotel[insercao_quarto].pop()


    #Inicia a variácel que incrementa a posição na lista interna e zera para a inserção seguinte
    slot_quarto = 0

    #Looping interno para cadastro dos hópedes (nome e cpf) conforme quantidade informada
    for i in range(qde_hospedes):

        #Solicita o nome do hóspede
        nome_hospede = input("Digite o nome do hospede\n")#
        if nome_hospede == 'fim': #Opção de saída do looping
            #del hotel[insercao_quarto]
            break

        #Coloca o nome na posição da lista hotel
        hotel[insercao_quarto].insert(slot_quarto,nome_hospede)

        #Incrementa posição na lista interna para receber o CPF
        slot_quarto += 1

        #Solicita o número do CPF
        cpf = int(input("Digite o número do CPF do hóspede\n"))

        #Insere CPF na lista
        hotel[insercao_quarto].insert(slot_quarto,cpf)

        #Incrementa posição na lista interna
        slot_quarto += 1



    #Fora do looping interno

    #Posiciona inserção no novo quarto
    insercao_quarto += 1


#Mostra quartos com os hóspedes e seus CPFs
print(hotel)