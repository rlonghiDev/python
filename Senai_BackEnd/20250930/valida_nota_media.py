import time
avaliacao = []


#Função para verificar erro de digitação e caracter não autorizado

def valida(valida):
    ponto_ou_virgula = 0 
    for c in nota_str:
        if c == '.':
            ponto_ou_virgula += 1
        
        #Verifica caracter diferente de digito no numero, excessão ao ponto "."
        if not c.isdigit() and c != '.':
            print("Número inválido, tente novamente")
            time.sleep(3)
            valida = "ruim"
            break


    #Verifica erro de digitação, inclusão de mais que um ponto ou vírgula
    if ponto_ou_virgula > 1:
        print("Número inválido, tente novamente")
        time.sleep(3)
        valida = "ruim"
    ponto_ou_virgula = 0 
    
    return(valida)




while True:
    nota_str = input("Digite a nota do aluno ou F para finalizar\n")
    
    #Encerra looping e passa para os cálculos e mensagens finais 
    if nota_str == 'F' or nota_str == 'f':
        break

    #Substitui vírgula por ponto
    nota_str = nota_str.replace(",", ".")
    
    #Coloquei esse trecho numa função porque se houvesse problema os comandos break e continue só afetariam o looping interno.
    #O erro acabaria passando. A ideia foi criar uma bandeira (flag) de problema e forçar o retorno para o inicio do looping
    nota_str = valida(nota_str)
    print("validacao:",nota_str)

    
    #transforma string em float
    if nota_str != 'ruim':
        nota_num = float(nota_str)
    else:
        continue
    

    # Verifica intervalo da nota entre 0.0 e 10.0
    if nota_num < 0.0 or nota_num > 10.0:
        print("Nota fora do intervalor entre 0 a 10. Por favor tente novamente.")
        time.sleep(3)
    
    else:
        #Adiciona a nota a lista avaliação
        avaliacao.append(nota_num)

#Soma todos os itens da lista
soma_pontos = sum(avaliacao)

#Obtém o número de notas na lista
qde_notas = len(avaliacao)


#Cálculo simples da média
media = soma_pontos/qde_notas


#Mensagem final com os resultados
print(f"o aluno foi avaliado {qde_notas} vezes e obteve a media de {round(media,2)}")




    
    