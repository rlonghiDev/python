import tkinter as tk

# Função para exibir uma mensagem quando o botão for clicado
def exibir_mensagem():
  print("O botão foi clicado!")

# Criar uma janela
janela = tk.Tk()
janela.title("Botão Simples")

# Adicionar um botão
botao = tk.Button(janela, text="Clique Aqui", command=exibir_mensagem)
botao.pack()

# Executar o loop principal
janela.mainloop()