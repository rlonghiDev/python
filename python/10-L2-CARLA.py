"""
Carla Borba Brandão Longhi
Enunciado: 
Crie um programa em Python que simule um sistema de login com senha. O programa deve
permitir ao usuário tentar até 3 vezes inserir a senha correta. Se a senha inserida estiver correta, o
programa deve exibir uma mensagem de boas-vindas. Se a senha estiver errada após 3 tentativas,
o programa deve exibir uma mensagem de erro.
(a) O programa deve armazenar uma senha fixa (por exemplo, ”senha123”).
(b) O programa deve permitir ao usuário tentar inserir a senha até 3 vezes. Para cada tentativa,
o programa deve verificar se a senha está correta utilizando a estrutura if.
(c) Caso a senha esteja correta, o programa deve exibir uma mensagem de boas-vindas e encer-
rar o loop de tentativas.
(d) Caso a senha esteja errada após 3 tentativas, o programa deve exibir uma mensagem de erro
e finalizar a execução.
(e) Utilize o while para controlar o número de tentativas e o for para iterar sobre as tentativas
de senha.
"""
contador = 1
while contador < 4:
    password = input("Digite a senha: ")
    if password == 'senha123':
        print("Olá ! Seja bem vindo(a)")
        exit()
    contador += 1
print("Erro na senha, tente novamente mais tarde")
