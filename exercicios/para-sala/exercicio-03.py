# 3. Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.

def nome(resposta):
    if resposta == "Sim" or resposta == "sim":
        print("Que maravilha!")
    elif resposta == "Não" or resposta == "não":
        print("Que triste")

inserir_nome = input("Insira o seu nome: ") 
gostar_nome = input("Você gosta do seu nome? ")

nome(gostar_nome)


