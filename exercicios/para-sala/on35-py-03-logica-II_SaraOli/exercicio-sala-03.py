# 3.Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.

def afinidadeNome(gostaNaoGosta):
    if gostaNaoGosta == 'Sim':
        return 'Que incrível, fico feliz que você curte seu nome!'
    else:
        return 'Que poxa! Como seria o nome que você se daria? '
    
qual_seu_nome = str(input('Qual seu nome? '))
resultado_nome = str(input('Você gosta do seu nome? '))

resultado_gostaNome = afinidadeNome(resultado_nome)

print(resultado_gostaNome)
    