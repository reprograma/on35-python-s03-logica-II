#Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, 
#em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.

def perguntar_nome(resposta):
    if resposta == "sim":
        return "Que maravilha! Eu também gosto do meu."
    elif resposta == "não":
        return "Sinto muito, espero que consiga ser chamado como deseja"

nome = input("Qual o seu primeiro nome? ")
gostar = input("Você gosta do seu nome? ")    

responder = print(perguntar_nome(gostar))