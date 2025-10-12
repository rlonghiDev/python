# word = input("Please, type a word\n")
# word_upper = word.upper()

# for letter in word_upper:
#     if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
#         continue
#     print(letter)

# blocos_usuario = int(input("Informe o número de blocos que serão utilizados\n"))
# contador = 0
# blocos_utilizados = 0
# while blocos_usuario > blocos_utilizados:
#     blocos_utilizados +=1
#     blocos_usuario = blocos_usuario - blocos_utilizados
#     contador += 1
#     #print('*' * blocos_utilizados)


# print("\nA altura da pirâmide é:",contador)


c0 = int(input("Insira um número inteiro diferente de zero e um\n"))
i = 0

while c0 != 1:
    if (c0 % 2) == 0:
        c0 = c0 // 2
        print(c0)
    else:
        c0 = 3 * c0 + 1
        print(c0)
    i += 1

print("Etapas:",i)
