meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]
#seu código aqui
#Inicia contador de looping principal
c = 0 

#Inicia lista de vendedores acima da meta
vendedor_acima = [[]]
#Inicia contador para inserção de vendas acima da meta, indicará posição na sub-lista
i = 0


#Itera a lista para verificar o cumprimento da meta
for v in range(len(vendas)):

    #Verifica se a meta foi cumprida e captura nome e valor de venda
    if vendas[c][1] > meta:
        
        
        #Cria posição vazia na lista para inserir vendedores e metas depois da primeira inserção
        if i > 0:
            vendedor_acima.append([''])
            #Limpa string vazia usada para criar posição na lista, a posição fica vazia 
            vendedor_acima[i].pop()
            
        #Insere o nome na posição da sub-lista
        vendedor_acima[i].insert(0,vendas[c][0])
        
        #Insere valor das vendas
        vendedor_acima[i].insert(1,vendas[c][1])

        #Indica próxima posição na sub-lista
        i += 1      

    #Incrementa contador
    c += 1


print("Vendedores acima da meta separados em su-listas: Uma linha e várias colunas\n")
print(vendedor_acima)
