"""
Carla Borba Brandão Longhi
Enunciado: 
Faça um programa na Linguagem Python que leia 2 números e em seguida pergunte ao usuário
qual operação ele deseja realizar (soma, subtração, divisão ou multiplicação). O resultado da
operação deve ser acompanhado de uma frase que diga se o resultado da operação é:
• par ou ı́mpar;
• positivo ou negativo;
• inteiro ou decimal
"""
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

operacao = input(" Digite S para somar, SUB para subtrair,M para multiplicar e D para dividir: ")

match operacao:
    case 'S':
        resultado = numero1 + numero2
    case 'SUB':
        resultado = numero1 - numero2
    case 'M':
        resultado= numero1 * numero2
    case 'D':
        resultado = numero1 / numero2
    case _:
        print("Opção inválida, tente novamente.")
        exit()

num_par = resultado % 2
if num_par == 0:
    par = 'par'
else:
    par = 'ímpar'

if resultado < 0:
    negativo = 'negativo'
else:
    negativo = 'positivo'

num_decimal = int(resultado) - resultado
if num_decimal != 0:
   decimal = 'decimal'
else:
    decimal = 'inteiro'

print("O resultado da operação é: ",resultado,". Este número é: ",par,",",negativo,"e",decimal,".")
