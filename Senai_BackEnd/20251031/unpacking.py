vendas = [ 1000,2000,300,300,150]
funcionarios = ['João', 'Lira','Ana','Maria','Paula']

for item in enumerate(vendas):
    i,vendas = item
    print(f"O funcionário {funcionarios[i]} vendeu {vendas}")