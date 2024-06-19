#Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.

def pergunta(resposta):

    if  resposta == "sim":
        print("Eu também amo este nome \n")
    else:
        print("Entendo mas ainda assim é um belo nome \n")


input ("Como se chama seu Doguinho? \n")
resposta_nome_do_doguinho = input ("Você gosta do nome dele?\n")
resultado = (resposta_nome_do_doguinho)

pergunta(resposta_nome_do_doguinho)