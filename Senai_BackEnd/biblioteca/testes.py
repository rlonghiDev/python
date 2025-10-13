## Relatório Livro ##











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

# posicao = registro.find('Registro')
# tamanho = len(registro)

# reg = '0'
# trecho_inteiro = registro[posicao:tamanho]
# for i in trecho_inteiro:
#     if i.isdigit():
#         reg += i


# valor = int(reg) + 1


# print("Registro:", valor)

