#Coleta de dados
precoInicial = float(input("Informe o preço do produto\n"))
desconto = float(input("Informe o desconto a ser aplicado (usar ponto para separar casas decimais)\n"))

#Processamento
descontoConvertido = desconto/100
PrecoComDesconto = precoInicial * (1 - descontoConvertido)

#Saída
print("O valor com deconto é: ", PrecoComDesconto)