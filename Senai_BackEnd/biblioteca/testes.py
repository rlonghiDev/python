## Relatório Livro ##

def monta_string(dict):
    linha1 = '#' * 50
    str2 = 'Título: '+ dict['nome']
    linha2 = '#' + str2.center(48) + '#'
    str3 = 'Autor: '+ dict['autor']
    linha3 = '#' + str3.center(48) + '#'
    str4 = 'Disponível: '+ str(dict['Qde_disp'])
    linha4 = '#' + str4.center(48) + '#'

    print(linha1 +'\n'+ linha2 + '\n' + linha3)




with open("livros.txt","r") as arq:
    for linha in arq:
        dicionario = eval(linha)
        monta_string(dicionario)
        # print('#' * 30)
        # print('#'+ ' ' * 28 + '#')
        # print(f'#      Título: {dicionario['nome']}  #')
        # print(f'#       Autor: {dicionario['autor']} #')
        # print(f'# Disponíveis: {dicionario['Quantidade disponível']}     # ')
        
        
        
        
        
        # for (chave,valor) in (dicionario.items()):
        #     print(f"{chave},{valor}")
        

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

