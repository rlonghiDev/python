valorEmReais = float(input("Digite o valor em Reais (BRL)\n"))
#dolar Ptax em 20/08/2025 ->5,4649
taxaDeCambio = 5.4649
valorEmDolar = valorEmReais/taxaDeCambio
print("O valor convertido para Dólares é: (USD)",round(valorEmDolar,2))