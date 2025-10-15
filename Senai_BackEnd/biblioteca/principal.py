import time
import datetime

while True:
    print("""
          Bem vindo ao sistema gerenciador de livros !
          
          Escolha a opção desejada:
          1 - Cadastrar um livro
          2 - Cadastrar um leitor
          3 - Cadastrar um empréstimo 
          4 - Imprimir um relatório
          5 - Sair 

          """)
    
    #Recebe a escolha e verifica opção válida
    menu_principal = input("Digite a opção desejada\n")
    if menu_principal != '1' and menu_principal != '2' and menu_principal != '3' and menu_principal != '4' and menu_principal != '5':
        print("Opção incorreta, tente novamente")
        time.sleep(3)
        continue
    
    ######Saída do Looping #####
    if menu_principal =='5':
        break
    
    ####Início Cadastra Livro ###

    def procura_ultimo_registro(tipo_procura):
        
        if tipo_procura == 'livro':
            arquivo_para_abrir = "livros.txt"
        if tipo_procura == 'leitor':
            arquivo_para_abrir = "leitores.txt"

        with open(arquivo_para_abrir,"r") as arq:
            linha = arq.readlines()

        arq.close()

        if linha:
            registro = linha[-1].strip()
        else:
            registro = '1'

        posicao = registro.find('Registro')
        tamanho = len(registro)
        print("Posição:",posicao,"Tamanho:",tamanho)

        reg = '0'
        trecho_final = registro[posicao:tamanho]
        for i in trecho_final:
            if i.isdigit():
                reg += i

        valor = int(reg) + 1
        return valor

    def cadastrar_livro():

        #Produra o último registro de livro para partir determinar próximo registro.
        num_registro = procura_ultimo_registro('livro')

        #Recebe os dados do livro 
        nome = input("Digite o nome do livro\n")
        autor = input("Digite o nome do autor\n")
        qde_disp = int(input("Digite a quantidade disponível do livro\n"))
        qde_uso = 0
        

        livro_dicionario = {}
        livro_dicionario['nome'] = nome
        livro_dicionario['autor'] = autor
        livro_dicionario['Qde_disp'] = qde_disp
        livro_dicionario['Qde_uso'] = qde_uso
        livro_dicionario['Registro'] = num_registro

        livro_str = str(livro_dicionario) + '\n'

        with open ("livros.txt", "at") as arq:
            arq.write(livro_str)
        
        arq.close()
    
    if menu_principal == '1':
        cadastrar_livro()
    
    #### Fim Cadastra Livro ####

    #### Início Cadastra Leitor ###

    def cadastrar_leitor():
        nome = input("Digite o nome do Leitor")
        escola = input("Informe qual escola está matriculado")
        turma = input("Informe o curso que o leitor está inscrito")
        ano_cadastro = datetime.date.today().year

        #Produra o último registro de livro para partir determinar próximo registro.
        registro_leitor = procura_ultimo_registro('leitor')

        leitor ={}
        leitor['nome']=nome
        leitor['escola']=escola
        leitor['turma'] = turma
        leitor['ano']=ano_cadastro
        leitor['Registro'] = registro_leitor

        leitor_str = str(leitor) + '\n'

        with open("leitores.txt","at") as arq:
            arq.write(leitor_str)

        arq.close()

    if menu_principal == '2':
        cadastrar_leitor()

    ### Final Cadastra Leitor ###

    ### Relatório Livros ###

    
    def monta_string_livro(dict):
        linha1 = '#' * 44
        espacamento = '#' + ' ' * 42 + '#'
        str21 = 'Título: ' # String [linha2] [posição1]
        str22 = dict['nome'] # String [linha2] [posição1]
        linha2 = '#' + str21.rjust(21) + str22.ljust(21) + '#'
        str31 = 'Autor: '
        str32 = dict['autor']
        linha3 = '#' + str31.rjust(21) + str32.ljust(21) + '#'
        str41 = 'Disponível: '
        str42 = str(dict['Qde_disp'])
        linha4 = '#' + str41.rjust(21) + str42.ljust(21) + '#'
        str51 = 'Registro: '
        str52 = str(dict['Registro'])
        linha5 = '#' + str51.rjust(21) + str52.ljust(21) + '#'

        ficha = (linha1 +'\n'+ espacamento + '\n' + linha2 + '\n' + linha3 + '\n' + linha4 + '\n' + linha5 + '\n' + espacamento + '\n' + linha1 + '\n')
        return ficha


   
    def relatorio_livros():
        with open("livros.txt","r") as arq:
            
            for linha in arq:
                dicionario = eval(linha)
                ficha = monta_string_livro(dicionario)
                    
                print(ficha)
            
            arq.close()#Fecha arquivo

    ####### Final Relatório Livros ####


    ##### Relatório de Leitores ####

    def monta_string_leitor(dict):
        linha1 = '#' * 44
        espacamento = '#' + ' ' * 42 + '#'
        str21 = 'Nome: ' # String [linha2] [posição1]
        str22 = dict['nome'] # String [linha2] [posição1]
        linha2 = '#' + str21.rjust(21) + str22.ljust(21) + '#'
        str31 = 'Escola: '
        str32 = dict['escola']
        linha3 = '#' + str31.rjust(21) + str32.ljust(21) + '#'
        str41 = 'Turma: '
        str42 = str(dict['turma'])
        linha4 = '#' + str41.rjust(21) + str42.ljust(21) + '#'
        str51 = 'Registro: '
        str52 = str(dict['Registro'])
        linha5 = '#' + str51.rjust(21) + str52.ljust(21) + '#'
        str61 = 'Ano: '
        str62 = str(dict['ano'])
        linha6 = '#' + str61.rjust(21) + str62.ljust(21) + '#'

        ficha = (linha1 +'\n'+ espacamento + '\n' + linha2 + '\n' + linha3 + '\n' + linha4 + '\n' + linha5 + '\n' + linha6 + '\n' + espacamento + '\n' + linha1 + '\n')
        return ficha


   
    def relatorio_leitores():
        with open("leitores.txt","r") as arq:
            
            for linha in arq:
                dicionario = eval(linha)
                ficha = monta_string_leitor(dicionario)
                    
                print(ficha)
            
            arq.close()#Fecha arquivo


    if menu_principal == '4':

        while True:

            print("""
                Digite 1 para relatório de livros
                Digite 2 para relatório de leitores
                Digite 3 para relatório de empréstimos
                Digite 4 para voltar ao menu principal

                """)

            outra_escolha = input("Informe a opção desejada: \n")
        

            if outra_escolha == '4':
                break

            if outra_escolha == '1':
                relatorio_livros()

            if outra_escolha == '2':
                relatorio_leitores()

    ##### Final Relatório Leitores ######

    ### Cadastro de Empréstimo ####

     if menu_principal == '3':

        while True:

            print("""

                Digite 1 para informar o empréstimo
                Digite 2 para informar devolução
                Digite 3 para voltar
                  
                """)
            
            opcao = input("Informe o que deseja fazer")

            if opcao == '5':
                break

            if opcao == '1': # Informar Empréstimo 



            if opcao == '2':

                

