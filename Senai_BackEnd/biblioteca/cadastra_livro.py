import ultimo_registro
import json

def cadastrar_livro():

    #Produra o último registro de livro para partir determinar próximo registro.
    num_registro = ultimo_registro.procura_ultimo_registro('livro')

    #Recebe os dados do livro 
    nome = input("Digite o nome do livro\n")
    autor = input("Digite o nome do autor\n")
    qde_disp = int(input("Digite a quantidade disponível do livro\n"))
    qde_uso = 0
    

    livro_dicionario = {}
    livro_dicionario['nome'] = nome
    livro_dicionario['autor'] = autor
    livro_dicionario['Qde_disp'] = qde_disp
    livro_dicionario['Qde_uso'] = qde_uso
    livro_dicionario['Registro'] = num_registro

    livro_str = json.dumps(livro_dicionario) + '\n'

    with open ("livros.txt", "at") as arq:
        arq.write(livro_str)
    
    arq.close()