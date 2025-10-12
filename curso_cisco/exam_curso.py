#Tic tac toe

# Sua tarefa é escrever um programa simples que finge jogar tic-tac-toe com o usuário. Para tornar tudo mais fácil para você, decidimos simplificar o jogo. Aqui estão nossas suposições:

# o computador (ou seja, seu programa) deve jogar usando 'X's;
# o usuário (por exemplo, você) deve jogar usando 'O's;
# o primeiro movimento pertence ao computador - ele sempre coloca seu primeiro 'X' no meio do quadro;
# todos os quadrados são numerados linha por linha, começando com 1 (consulte a sessão de exemplo abaixo para referência)
# o usuário insere seu movimento inserindo o número do quadrado escolhido - o número deve ser válido, ou seja, deve ser um número inteiro, deve ser maior que 0 e menor que 10, e não pode apontar para um campo que já está ocupada;
# o programa verifica se o jogo acabou - há quatro veredictos possíveis: o jogo deve continuar, o jogo termina com um empate, você ganha ou o computador ganha;
# o computador responde seu movimento e a verificação é repetida;
# não implementem qualquer forma de inteligência artificial - uma escolha de campo aleatória feita pelo computador é boa o suficiente para o jogo.

import random

tabuleiro = [[1,2,3],[4,5,6],[7,8,9]]


while True:

    print("Você está jogando com a marcação 'O', informe o número da posição que deseja colocar sua marca./nSe não houver um número a posição já recebeu uma jogada e não pode mais ser escolhida\n")
    escolha_oponente = input("Escolha a posição para a jogada\n")

    if escolha_oponente == 'F':
        break

    escolha_oponente = int(escolha_oponente)

    def jogada_oponente(livre):
        if livre == 1 or livre == 2 or livre == 3:
            pos3 = 0
            if livre == 1:
                pos4 = 0
            if livre == 2:
                pos4 = 1
            if livre == 3:
                pos4 = 2

        if livre == 4 or livre == 5 or livre == 6:
            pos3 = 1
            if livre == 4:
                pos4 = 0
            if livre == 5:
                pos4 = 1
            if livre == 6:
                pos4 = 2

        if livre == 7 or livre == 8 or livre == 9:
            pos3 = 2
            if livre == 7:
                pos4 = 0
            if livre == 8:
                pos4 = 1
            if livre == 9:
                pos4 = 2

        return pos3,pos4


    def verifica_livre(p1,p2):
        verifica_posicao = tabuleiro[p1][p2]
        if verifica_posicao != 'X' or verifica_posicao != 'O':
            tabuleiro[p1][p2] = 'O'
        else:
            print("Posição ocupada, escolha outra")









    def separacao():
        global traco
        traco = '+'
        for i in range(3):
            traco = traco + (7 * '-')
            traco += '+'
        return traco

    def linha_vertical():
        global linha
        linha = '|'
        for i in range(3):
            linha = linha + (7 * ' ')
            linha += '|'

        return linha

    def param1(posicao):
        global param
        param = '|'
        j = 0
        for x in range(3):
            for i in range(6):
                param += ' '
                if i == 2:
                    tab = str(tabuleiro[posicao][j])
                    param += tab
                    j += 1
                if i == 5:
                    param += '|'

        return param

    def jogada():
        pos1 = random.randint(0,2)
        pos2 = random.randint(0,2)
        verifica_posicao = tabuleiro[pos1][pos2]
        if verifica_posicao != 'X' or verifica_posicao != 'O':
            tabuleiro[pos1][pos2] = 'X'
        else:
            jogada()


    p1, p2 = jogada_oponente(escolha_oponente)
    verifica_livre(p1,p2)
    jogada()


    print("\n",separacao(),"\n",linha_vertical(),"\n",param1(0),"\n",linha_vertical(),"\n",separacao(),"\n",linha_vertical(),"\n",param1(1),"\n",linha_vertical(),"\n",separacao(),"\n",linha_vertical(),"\n",param1(2),"\n",linha_vertical(),"\n",separacao())


 # A função aceita um parâmetro contendo o status atual da placa
 # e o imprime no console.


#def enter_move(board):
 # A função aceita o status atual do tabuleiro, pergunta ao usuário sobre sua jogada, 
 # verifica a entrada e atualiza o quadro de acordo com a decisão do usuário.


#def make_list_of_free_fields(board):
 # A função navega pelo tabuleiro e constrói uma lista de todas as casas livres; 
 # a lista consiste em tuplas, enquanto cada tupla é um par de números de linha e coluna.
