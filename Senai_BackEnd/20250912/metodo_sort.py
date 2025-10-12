my_list = [8, 10, 6, 2, 4]  # Lista para ordenar
swapped = True  # É um pouco falso, precisamos dele para entrar no loop while.
count = 0
while swapped:
    swapped = False  # nenhuma troca até agora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # uma troca ocorreu!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            count += 1
 
print(my_list,count)

#Interativo
# my_list = []
# swapped = True
# num = int(input("Quantos elementos você deseja embaralhar? "))

# for i in range(num):
#  val = float(input("Entre com a lista de elementos:"))
#  my_list.append(val)

# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print("\nSorted:")
# print(my_list)

#Função no Python
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

#Método reverse - inverte a ordem
lst = [5, 3, 1, 2, 4]
print(lst)
 
lst.reverse()
print(lst)  # outputs: [4, 2, 1, 3, 5]