import ultimo_registro
import json
import datetime

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

##### Relatorio Livro #####

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




##### Relatório de Empréstimo #####

#### String Emprestimo ####
def busca_info(Registro, tipo):
    
    if tipo == 'leitor':
        arquivo_para_ler = "leitores.txt"
        
    if tipo == 'livro':
        arquivo_para_ler = "livros.txt"
        
    if tipo == 'emprestimo':
        arquivo_para_ler = "emprestimos.txt"
    
    with open(arquivo_para_ler,"r") as arq:
        
        for linha in arq:
            dicionario = eval(linha)
            
            if dicionario["Registro"] == Registro:
                nome = dicionario["nome"]
                
    arq.close()#Fecha arquivo
    
    return nome


    


def monta_string_emprestimo(dict):
    linha1 = '#' * 44
    espacamento = '#' + ' ' * 42 + '#'
    titulo = 'EMPRESTIMO DE LIVRO'
    linha1a = '#' + titulo.center(42) + '#'
    str21 = 'Leitor: ' # String [linha2] [posição1]
    str22 = busca_info(int(dict["leitor"]),"leitor")
    linha2 = '#' + str21.rjust(21) + str22.ljust(21) + '#'
    str31 = 'livro: '
    str32 = busca_info(int(dict["livro"]),"livro")
    linha3 = '#' + str31.rjust(21) + str32.ljust(21) + '#'
    str41 = 'Emprestado em: '
    str42 = str(dict["data"])
    linha4 = '#' + str41.rjust(21) + str42.ljust(21) + '#'
    str51 = 'Registro: '
    str52 = str(dict['Registro'])
    linha5 = '#' + str51.rjust(21) + str52.ljust(21) + '#'

    ficha = (linha1 +'\n'+ espacamento + '\n' + linha1a + '\n' + linha2 + '\n' + linha3 + '\n' + linha4 + '\n' + linha5 + '\n' + espacamento + '\n' + linha1 + '\n')
    
    return ficha


def relatorio_emprestimo():
    
    with open("emprestimos.txt","r") as arq:
        
        for linha in arq:
            dicionario = eval(linha)
            ficha = monta_string_emprestimo(dicionario)
                
            print(ficha)
        
    arq.close()#Fecha arquivo

    
    
    
    




