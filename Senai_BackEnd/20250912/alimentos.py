
import time
categoria = 0
nome_produto = ''
quantidade_produto = 0




while categoria != -1 or nome_produto != '-1' or quantidade_produto != -1:
    print("Digite o código da categoria de produto conforme segue:\n1 para Alimentos\n2 para bebidas\n3 para limpeza\npara encerrar -1")
    categoria = input()
    if categoria == '':
         categoria = 4
    else:
         categoria = int(categoria
                         )
    if categoria == -1: 
        break
    nome_produto = input("Digite o nome do produto\n")
    print(nome_produto, type(nome_produto))

    quantidade_produto = input("Digite a quantidade do produto\n")

    print(quantidade_produto, type(quantidade_produto))

    if quantidade_produto == None or quantidade_produto == '':
            quantidade_produto = -1
    else:
         quantidade_produto = int(quantidade_produto)

    print(quantidade_produto)

    if (categoria != 1 and categoria != 2 and categoria != 3) or (nome_produto == None) or quantidade_produto == -1:
        print("Aconteceu algum erra na digitação, por favor tente novamente")
        time.sleep(7)
        continue

    if categoria == 1 and quantidade_produto < 50:
        print(f"Solicitar {nome_produto} à equipe de compras, temos apenas {quantidade_produto} em estoque (Quantidade mínima 50 unid)\n")
        time.sleep(5)
    elif categoria == 2 and quantidade_produto < 75:
        print(f"Solicitar {nome_produto} à equipe de compras, temos apenas {quantidade_produto} em estoque (Quantidade mínima 75 unid)\n")
        time.sleep(5)
    elif categoria == 3 and quantidade_produto < 30:
        print(f"Solicitar {nome_produto} à equipe de compras, temos apenas {quantidade_produto} em estoque (Quantidade mínima 30 unid)\n")
        time.sleep(5)
    else:
        continue
