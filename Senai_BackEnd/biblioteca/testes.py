## Relatório Livro ##

def monta_string(dict):
    linha1 = '#' * 50
    espacamento = '#' + ' ' * 48 + '#'
    str21 = 'Título: ' # String [linha2] [posição1]
    str22 = dict['nome'] # String [linha2] [posição1]
    linha2 = '#' + str21.rjust(24) + str22.ljust(24) + '#'
    str31 = 'Autor: '
    str32 = dict['autor']
    linha3 = '#' + str31.rjust(24) + str32.ljust(24) + '#'
    str41 = 'Disponível: '
    str42 = str(dict['Qde_disp'])
    linha4 = '#' + str41.rjust(24) + str42.ljust(24) + '#'
    str51 = 'Registro: '
    str52 = str(dict['Registro'])
    linha5 = '#' + str51.rjust(24) + str52.ljust(24) + '#'

    ficha = (linha1 +'\n'+ espacamento + '\n' + linha2 + '\n' + linha3 + '\n' + linha4 + '\n' + linha5 + '\n' + espacamento + '\n' + linha1 + '\n')
    return ficha


with open("livros.txt","r") as arq:
    
    for linha in arq:
        dicionario = eval(linha)
        ficha = monta_string(dicionario)
            
        print(ficha)
            
        



        
#tabulate

arq.close()


# string_customizada = "nome:Charlie,idade:35,cidade:Nova York"
# # Divide a string em pares chave:valor e depois em chave e valor
# meu_dicionario = {chave.strip(): valor.strip() for item in string_customizada.split(',') for chave, valor in [item.split(':')]}

# print(meu_dicionario)
# print(type(meu_dicionario))






# import datetime

# nome = input("Digite o nome do Leitor")
# escola = input("Informe qual escola está matriculado")
# turma = input("Informe o curso que o leitor está inscrito")
# ano_cadastro = datetime.date.today().year
# registro_leitor = ''

# leitor ={}
# leitor['nome']=nome
# leitor['escola']=escola
# leitor['turma'] = turma
# leitor['ano']=ano_cadastro
# leitor['Registro'] = registro_leitor

# leitor_str = str(leitor) + '\n'

# with open("leitores.txt","at") as arq:
#      arq.write(leitor_str)

# arq.close()








# with open("livros.txt","r") as arq:
#     linha = arq.readlines()

# arq.close()

# if linha:
#     registro = linha[-1].strip()
# else:
#     registro = 'falhou'
#     print(registro)


# print(type(registro))

# posicao = registro.find('Registro')
# tamanho = len(registro)

# reg = '0'
# trecho_inteiro = registro[posicao:tamanho]
# for i in trecho_inteiro:
#     if i.isdigit():
#         reg += i


# valor = int(reg) + 1


# print("Registro:", valor)

