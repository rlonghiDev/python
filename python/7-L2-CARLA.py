"""
Carla Borba Brandão Longhi
Enunciado: 
Crie um programa em Python que peça ao usuário a senha “123senai”. Se a senha for incorreta,
continuar pedindo até que a senha esteja correta. Em seguida, o usuário deve ter acesso a um
gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário
deve informar de qual número ele deseja ver a tabuada. Se o número inserido for par, mostrar a
tabuada dos números pares. Se não, imprimir os números ı́mpares
"""
senha =''
contador = 0
while senha != '123senai':
    senha = input("Digite a senha: ")

numerotabuada = int(input("Digite um valor de zero a dez: "))
testeparidade = numerotabuada % 2
if testeparidade > 0:
    paridade ='impar'
else:
    paridade = 'par'



if paridade == 'par':
    par = 0


    while par < 11:
        print("\n-- tabuada do: ",par)

        while contador < 11:
            resultado = contador*par
            print(contador,"x",par,"=",resultado)
            contador +=1
    
        contador = 0
        
        par += 2

else:
    impar = 1
    
    while impar < 11:
        print("\n-- tabuada do: ",impar)
        while contador < 11:
            resultado = contador*impar
            print(contador,"x",impar,"=",resultado)
            contador +=1
        
        contador = 0
        impar += 2


