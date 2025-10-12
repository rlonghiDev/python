#from main import dobrar, triplicar, quadrad
from calculo import dobro, triplo, quadrado

def operacoes():
    while True:
        print("Verifique as opções abaixo:")
        print("""
            1 - Calcular o dobro
            2 - Calcular o triplo
            3 - Calcular o quadrado
            4 - Finalizar          
            """)
        
        escolha = int(input("Qual é sua escolha ?"))
        
        # saída do looping 
        if escolha == 4:
            break
        
        numero = int(input("Digite o número inteiro"))
        
        
        
        def dobrar(x):
            global dobro
            dobro = dobro(x)
            print(f"\nO dobro de {x} é {dobro}\n")


        # y = input("Agora, digite outro numero e vou dizer o triplo")


        def triplicar(y):
            global triplo
            triplo = triplo(y)
            print(f"\nO triplo de {y} é {triplo}\n")

        # z = int(input("Agora outro número para te dizer o quadrado ..."))

        def quadrad(z):
            global quadrado
            quadrado = quadrado(z)
            print(f"\nO quadrado de {z} é {quadrado}\n")
                
        if escolha == 1:
            dobrar(numero)
            
        if escolha == 2:
            triplicar(numero)
            
        if escolha == 3: 
            quadrad(numero)
        
        