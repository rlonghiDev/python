import json
import datetime
import ultimo_registro
import relatorios

def realiza_emprestimo(registro_leitor,registro_livro):
                
    with open("leitores.txt","r") as arq:
        global ficha_leitor
        global ficha_livro
        ficha_livro = {}
        ficha_leitor = {}

        for linha in arq:
            dicionario = eval(linha)
            if registro_leitor == dicionario['Registro']:
                ficha_leitor = dicionario
    
    arq.close()#Fecha arquivo

    with open("livros.txt", "r") as books:

        for linha in books:
            dict_books = eval(linha)
            if registro_livro == dict_books["Registro"]:
                ficha_livro = dict_books
    
    books.close()

    if ficha_leitor != None and ficha_livro != None:
        dict_emprestimo = {}
        dict_emprestimo['leitor'] = registro_leitor
        dict_emprestimo['livro'] = registro_livro
        dict_emprestimo['data'] = datetime.date.today()
        dict_emprestimo['Registro'] = ultimo_registro.procura_ultimo_registro('emprestimo')

    else:
        print("Erro, verifique os códigos de registro informados e tente novamente")
        exit(0)

    emprestimo_str = str(dict_emprestimo) + '\n'


    with open("emprestimos.txt","at") as arq:
        arq.write(emprestimo_str)

    arq.close()
    








def apaga_emprestimo():
    relatorios.relatorio_emprestimo()
    Registro = input("Digite o número do empréstimo que será encerrado")
    ficha_emprestimo = relatorios.busca_info(Registro,"Emprestimo")
    print(ficha_emprestimo)
    confirma = input("Confirma encerramento desse empréstimo ? s/n ")
    if confirma == 's':
        apaga_linha(Registro)
    
    if confirma == 'n':
        return
    
    