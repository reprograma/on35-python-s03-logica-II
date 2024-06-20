#Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.

nome = input("Qual é o seu nome? ")
pergunta = input("Você gosta do nome?")

if pergunta == 'sim':
    print('Que top, feliz por saber!')

elif pergunta == 'não':
    print(' Que pena, mas você pode mudar se tiver interesse')
    
