#3. Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.


def resposta(gosta_nome):
    if gosta_nome == "sim" or "Sim": 
        print(f'Que incrível que você gosta do seu nome, {nome}!')
    elif gosta_nome == "não" or "Não":
        print(f'Que pena que você não gosta do seu nome, {nome}!') 

nome = input("Insira seu nome: ")
pergunta_nome = input("Você gosta do seu nome? ")

resposta(pergunta_nome)


       

