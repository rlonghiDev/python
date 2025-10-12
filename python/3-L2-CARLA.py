"""
Carla Borba Brandão Longhi
Enunciado: 
Escreva um programa em Python que solicite ao usuário uma sequência de números separados
por espaço (por exemplo, ”2 4 6 8”). O programa deve usar um loop ‘for‘ para calcular a média
desses números e exibir o resultado.
"""

lista_string = input("Digite numeros separados por espaços: ").split(" ")

nova_lista = []

for i in lista_string:
        vira_numero = float(i)
        nova_lista.append(vira_numero)

soma = sum(nova_lista)
qtd_num = len(nova_lista)
media = soma/qtd_num
print("A média dos números digitados é: ",media)