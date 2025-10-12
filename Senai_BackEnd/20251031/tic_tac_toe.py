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
import os

#As jogadas irão acrescentar X ou O nas posições da Matriz conforme forem acontecendo
tabuleiro = [[1,2,3],[4,'X',6],[7,8,9]] #Primeira jogada é do computador na posição '5' 

while True:
    # ---- Composição do Tabuleiro ----

    #Limpa Console 
    os.system('clear')
  
    termina = False

    def encerra():
        global termina
        termina = 1


    #Separação superior e inferior e entre células
    def separacao():
        global traco
        traco = '+'
        for i in range(3):
            traco = traco + (7 * '-')
            traco += '+'
        return traco

    #Após separação 
    def linha_vertical():
        global linha 
        linha = '|'
        for i in range(3):
            linha = linha + (7 * ' ')
            linha += '|'

        return linha

    #Coleta a posição da Matriz para escrever o conteúdo de cada uma das nove células
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


    # ----- Estrutura do jogo -----

    #O oponente (humano) escolherá o número que está na célula do tabuleiro
    #A função abaixo transforma a escolha em posição na Matriz e retorna as coordenadas
    # e a indicação de que a jogada é do oponente através da variável usuario

    #Tabuleiro cheio ?

    def tabuleiro_cheio():
        i = 0 
        j = 0
        c = 0
        for i in tabuleiro:
            for j in range(3):
                conteudo_celula = i[j]
                if type(conteudo_celula) is int:
                    c += 1
                   
        if c == 0:
            print("O jogo acabou, resultado -> empate")
            print("\n",separacao(),"\n",linha_vertical(),"\n",param1(0),"\n",linha_vertical(),"\n",separacao(),"\n",linha_vertical(),"\n",param1(1),"\n",linha_vertical(),"\n",separacao(),"\n",linha_vertical(),"\n",param1(2),"\n",linha_vertical(),"\n",separacao())
            return True
        
        else:
            return False
    #Encerra o jogo se o tabuleiro estiver cheio
    if termina == 1:
        break



    #Função jogada do Usuário
    #Devolve a cooordenada na matriz que o Usuário escolheu e 
    #Identifica o "dono" da jogada

    def jogada_oponente(escolha):
        if escolha == 1 or escolha == 2 or escolha == 3:
            pos3 = 0
            if escolha == 1:
                pos4 = 0
            if escolha == 2:
                pos4 = 1
            if escolha == 3:
                pos4 = 2

        if escolha == 4 or escolha == 5 or escolha == 6:
            pos3 = 1 
            if escolha == 4:
                pos4 = 0
            if escolha == 5:
                pos4 = 1
            if escolha == 6:
                pos4 = 2

        if escolha == 7 or escolha == 8 or escolha == 9:
            pos3 = 2
            if escolha == 7:
                pos4 = 0
            if escolha == 8:
                pos4 = 1
            if escolha == 9:
                pos4 = 2 
        usuario = 0 


        return pos3,pos4,usuario


    #Função para jogada do computador 
    #Monta a jogada do computador de forma aleatória 
    #Retorna coordenadas e a indicação que a jogada vem do computador pela variuavel usuario
    def jogada_computador():
        pos1 = random.randint(0,2)
        pos2 = random.randint(0,2)
        usuario = 1 #Identifica que a jogada é do computador

        return pos1,pos2,usuario



    #Verifica célula livre e escreve no tabuleiro
    #Recebe as coordenadas e quem é o usuário
    def posicao_tabuleiro(p1,p2,usuario):
        
        #Recebe conteudo da matriz de controle
        verifica_posicao = tabuleiro[p1][p2]
        
               
        if verifica_posicao != 'X' and verifica_posicao != 'O':
            if usuario == 1:
                tabuleiro[p1][p2] = 'X' #Jogada computador
                return False,usuario
            if usuario == 0:
                tabuleiro[p1][p2] = 'O' #Jogada oponente
                return False,usuario
        else:
            if usuario == 1:
                return True, usuario
                
            
            if usuario == 0:
                return True, usuario
            
    
    #Verifica se houve ganhador
    def alguem_ganhou():
                
        #Verifica linhas
        for i in range(3):
            cont1 = tabuleiro[i][0]
            cont2 = tabuleiro[i][1]
            cont3 = tabuleiro[i][2]
                
            if cont1 == cont2 and cont2 == cont3:
                if cont1 == 'O':
                    ganhador = 'Usuário'
                    return True, ganhador
                else:
                    ganhador = 'Computador'
                    return True, ganhador

    
        #verifica colunas
        for i in range(3):
            cont1 = tabuleiro[0][i]
            cont2 = tabuleiro[1][i]
            cont3 = tabuleiro[2][i]
           
            if cont1 == cont2 and cont2 == cont3:
                if cont1 == 'O':
                    ganhador = 'Usuário'
                    return True, ganhador
                else:
                    ganhador = 'Computador'
                    return True, ganhador

        #Verifica diagonais
        cont1 = tabuleiro[0][0]
        cont2 = tabuleiro[1][1]
        cont3 = tabuleiro[2][2]
        if cont1 == cont2 and cont2 == cont3:
            if cont1 == 'O':
                    ganhador = 'Usuário'
                    return True,ganhador
            else:
                ganhador = 'Computador'
                return True,ganhador

        cont1 = tabuleiro[0][2]
        cont2 = tabuleiro[1][1]
        cont3 = tabuleiro[2][0]
        if cont1 == cont2 and cont2 == cont3:
            if cont1 == 'O':
                    ganhador = 'Usuário'
                    return True ,ganhador
            else:
                ganhador = 'Computador'
                return True, ganhador
            
        
        ganhador = None
        return False, ganhador




    #Mostra tabuleiro
    print("\n",separacao(),"\n",linha_vertical(),"\n",param1(0),"\n",linha_vertical(),"\n",separacao(),"\n",linha_vertical(),"\n",param1(1),"\n",linha_vertical(),"\n",separacao(),"\n",linha_vertical(),"\n",param1(2),"\n",linha_vertical(),"\n",separacao())


    #Informa condições do jogo ao Usuário e solicita jogada - encerra looping se teclar 't'
    print("Você está jogando com a marcação 'O', informe o número da posição que deseja colocar sua marca.\nSe não houver um número a posição já recebeu uma jogada e não pode mais ser escolhida\n")
    escolha_oponente = input("Escolha a posição para a jogada\nSe desejar encerrar tecle t + ENTER\n")

    if escolha_oponente == 't':
        break #Encerra looping e o jogo 
    else:
        escolha = int(escolha_oponente) #Converte variável em int

    #Chama função de jogada do oponente e recebe coordenadas nas variáveis
    p1,p2,usuario = jogada_oponente(escolha)

    
    #Chama a função para verificar se a célula está livre.
    celula_usada,usuario = posicao_tabuleiro(p1,p2,usuario)
    
    
    #Verifica se houve vencedor 
    venceu, vencedor = alguem_ganhou()

    if venceu:
        print("O ganhador foi: ",vencedor)
        print("\n",separacao(),"\n",linha_vertical(),"\n",param1(0),"\n",linha_vertical(),"\n",separacao(),"\n",linha_vertical(),"\n",param1(1),"\n",linha_vertical(),"\n",separacao(),"\n",linha_vertical(),"\n",param1(2),"\n",linha_vertical(),"\n",separacao())
        break




    #Se a célula já estiver ocupada pede nova jogada para o Usuário
    tabuleiro_cheio()
    while celula_usada and usuario == 0:
        escolha_oponente = input("Célula ocupada, escolha uma posição livre\n")
        escolha = int(escolha_oponente)
        p1,p2,usuario = jogada_oponente(escolha)
        celula_usada,usuario = posicao_tabuleiro(p1,p2,usuario)
        

    
    #Jogada do computador
    p1,p2,usuario = jogada_computador()

    #Chama a função para verificar se a célula está livre.
    celula_usada,usuario = posicao_tabuleiro(p1,p2,usuario)


    #Verifica se houve vencedor
    venceu, vencedor = alguem_ganhou()
    
    if venceu:
        print("O ganhador foi: ",vencedor)
        print("\n",separacao(),"\n",linha_vertical(),"\n",param1(0),"\n",linha_vertical(),"\n",separacao(),"\n",linha_vertical(),"\n",param1(1),"\n",linha_vertical(),"\n",separacao(),"\n",linha_vertical(),"\n",param1(2),"\n",linha_vertical(),"\n",separacao())
        break


    #Verifica se a célula do tabuleiro está ocupada e "chama" nova jogada do Computador
    #Verifica também tabuleiro cheio

    while celula_usada and usuario == 1:
        p1,p2,usuario = jogada_computador()
        celula_usada,usuario = posicao_tabuleiro(p1,p2,usuario)
        venceu, vencedor = alguem_ganhou()
        termina = tabuleiro_cheio()
        
    
    if venceu:
        print("O ganhador foi: ",vencedor)
        print("\n",separacao(),"\n",linha_vertical(),"\n",param1(0),"\n",linha_vertical(),"\n",separacao(),"\n",linha_vertical(),"\n",param1(1),"\n",linha_vertical(),"\n",separacao(),"\n",linha_vertical(),"\n",param1(2),"\n",linha_vertical(),"\n",separacao())
        break
    
    if termina:
        break

    
    



                


    










 # A função aceita um parâmetro contendo o status atual da placa
 # e o imprime no console.


#def enter_move(board):
 # A função aceita o status atual do tabuleiro, pergunta ao usuário sobre sua jogada, 
 # verifica a entrada e atualiza o quadro de acordo com a decisão do usuário.


#def make_list_of_free_fields(board):
 # A função navega pelo tabuleiro e constrói uma lista de todas as casas escolhas; 
 # a lista consiste em tuplas, enquanto cada tupla é um par de números de linha e coluna.
