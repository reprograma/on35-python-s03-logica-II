# Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.

def gosta_do_nome(resposta):
    if resposta == 'sim':
        print('=D')
    elif resposta == 'nao':
        print ('=(')
    else:
        return 'Resposta Inválida'
    
nome_inserido = input('Digite um nome: ')
resposta = input('Você gosta do seu nome? (sim/nao)) ')

gosta_do_nome(resposta)

    

    