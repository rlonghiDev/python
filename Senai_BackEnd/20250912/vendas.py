## 3. Comparação com Ano Anterior

#Digamos que você está analisando as vendas de produtos de um ecommerce e quer identificar quais produtos tiveram no ano de 2020 mais vendas do que no ano de 2019, para reportar isso para a diretoria.
#Sua resposta pode ser um print de cada produto, qual foi a venda de 2019, a venda de 2020 e o % de crescimento de 2020 para 2019.
#Lembrando, para calcular o % de crescimento de um produto de um ano para o outro, podemos fazer: (vendas_produto2020/vendas_produto2019 - 1)
#Dica: lembre do enumerate, ele pode facilitar seu "for"

produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]


#Cria lista para receber incremento percentual de vendas
lista_incremento_vendas = []

#Lista para agrupar produto e resultado de vendas em sub-listas
lista_produto_resultado_venda = [[]]


for i, produto in enumerate(produtos):
    
    #Captura valores
    valor_venda_2019 = vendas2019[i]
    valor_venda_2020 = vendas2020[i]

    #Calcula o incremento das vendas
    incremento_vendas = round((valor_venda_2020/valor_venda_2019)-1,2)

    #Acrescenta resultado a lista
    lista_incremento_vendas.append(incremento_vendas)

    if i != 0:
        lista_produto_resultado_venda.append([""])
        lista_produto_resultado_venda[i].pop()
    
    lista_produto_resultado_venda[i].insert(0,produto)
    lista_produto_resultado_venda[i].insert(1,incremento_vendas)


#Lista de produtos em separado incremento de vendas
print(produtos)
print(lista_incremento_vendas)

#Lista em que o produto e o incrmento de vendas estão agrupados
print("\n")
print(lista_produto_resultado_venda)








