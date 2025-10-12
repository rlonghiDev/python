import tkinter as tk
from tkinter import messagebox

# faça o código aqui #

# Função para exibir uma mensagem quando o botão for clicado
def exibir_mensagem():
  messagebox.showinfo(title='Saudação', message='Olá !!!! Você clicou !!!!!')

# Criar uma janela
janela = tk.Tk()
janela.title("Botão Simples")

# Adicionar um botão
botao = tk.Button(janela, text="Clique Aqui", command=exibir_mensagem)
botao.pack()

# Executar o loop principal
janela.mainloop()