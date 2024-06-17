# Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, 
# em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.


def estabelecer_nome(confirmar_nome):
    if confirmar_nome == 'Sim':
        return 'Que bom que você gostou do seu nome!'
    else:
        return 'Que pena que você não gostou'
    
nome_usuario = input('Insira seu nome: ')
confirmar_nome = input('Você gostou do nome?\n a)Sim b)Não\nDigite sua resposta: ')
print(estabelecer_nome(confirmar_nome))