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
          5 - Sair """)
    
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
        livro_dicionario['Quantidade disponível'] = qde_disp
        livro_dicionario['Quantidade em uso'] = qde_uso
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

    