my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Escreva seu código aqui.
my_list2 = my_list[:] #Preserva a lista original intacta
tamanho2 = len(my_list2) #Referencia para o looping principal
tamanho = tamanho2 # Referencia para looping interno
i = 0 # Contador looping principal
# não pode ser utiizado looping tipo for porque o comando del altera o tamanho da lista e provoca o erro de "fora do range".

#O looping principal seleciona (fixa) o número que será comparado com os demais da lista
while tamanho2 > i:
    num1 = my_list2[i] #Número selecionado para comparação
    j = i + 1 #Contador do looping interno. Nunca pode apontar para a posição selecionada em (num1) porque pode apagá-la e com isso "perder" o número em análise
    
    #Looping interno analisa todas as demais posições depois da que foi selecionada pelo looping principal (j = i +1)
    while tamanho > j:
        if num1 == my_list2[j]: # Ao encontrar um número igual ao que está em análise permite executar código que apaga a posição.
            del my_list2[j] # Comando del altera o tamanho da lista e o conteúdo das posições posteriores a que foi apagada
            j -= 1 # Força o looping analisar novamente a mesma posição porque o seu conteúdo foi alterado.
            #Há um comando de incremento fora do if que posiciona a análise na mesma posição que foi apagada, o conteúdo mudou.
        
        tamanho = len(my_list2) # atualiza o tamanho da lista caso alguma posição tenha sido apagada
        j += 1 # Incrementa contador do looping interno 
       
    tamanho2 = len(my_list2)# Atualiza tamanho para looping principal depois das modificações executadas pelo looping interno 
    i += 1 #Incrementa contador do looping principal
    

            
#
print("A lista com os elementos exclusivos aqui")
print(my_list2) #Nova lista sem repetição dos itens.