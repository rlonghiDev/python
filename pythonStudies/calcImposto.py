valorRenda = float(input("Digite o valor da renda anual\n"))

if valorRenda <= 85528:
    valorImposto = (valorRenda * 0.18) - 556.02
    if valorImposto < 0:
        valorImposto = 0.0
else:
    valorImposto = 14839.02 + ((valorRenda - 85528) * 0.32)

print("O valor do imposto a ser pago é: ", round(valorImposto,0),"thallers")