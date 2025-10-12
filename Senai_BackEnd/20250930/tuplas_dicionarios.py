# school_class = {}

# while True:
#     name = input("Digite o nome do aluno: ")
#     #nome vazio "quebra" o looping
#     if name == '':
#         break

#     #Recebe a nota
#     score = int(input("Insira a pontuação do aluno (0-10): "))

#     #se a nota for fora do permitido o looping é quebrado
#     if score not in range(0, 11):
#         break

#     #se o nome do aluno já estiver no dicionário, aumente a tupla associada à nova pontuação (observe o operador + =)
#     if name in school_class:
#         school_class[name] += (score,)
#     #e este é um novo aluno (desconhecido para o dicionário), crie uma nova entrada - seu valor é uma tupla de um elemento que contém a pontuação inserida;
#     else:
#         school_class[name] = (score,)

# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#         print(name, ":", adding / counter)


# tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
# duplicates = tup.count(2)
# print(duplicates) # saídas: 4


# d1 = {'Adão Smith': 'A', 'Judy Paxton': 'B+'}
# d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
# d3 = {}
 
# for item in (d1, d2):
#    d3.update(item)
   
 
# print(d3)

#escreva um programa que converta a tupla colors em um dicionário.
# colors = (("green", "#008000"), ("blue", "#0000FF"))

# colors_dictionary = dict(colors)
# print(colors_dictionary)


colors = {
    "branco": (255, 255, 255),
    "cinza": (128, 128, 128),
    "vermelho": (255, 0, 0),
    "verde": (0, 128, 0)
    }
 
for col, rgb in colors.items():
    print(col, ":", rgb)
 