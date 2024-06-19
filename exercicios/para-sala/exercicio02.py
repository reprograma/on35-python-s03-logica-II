#Faça um programa que mostre na tela uma pergunta de múltipla escolha, e que, a partir da resposta do usuário, mostre na tela se ele acertou ou não.

def verifica_regiao(resposta):
    if resposta == 'norte':
        return 'Resposta Incorreta'
    elif resposta == 'sul':
        return 'Resposta Incorreta'
    elif resposta == 'sudeste':
        return 'Resposta Incorreta'
    elif resposta == 'nordeste':
        return 'Resposta Correta'
    elif resposta == 'centro oeste':
        return  'Resposta Incorreta'
    else:
        return 'Nao entendi sua resposta'
    
resposta_inserida = input('O estado da Bahia fica em qual regiao do Brasil? ')
resposta_elaborada = print(f"{verifica_regiao(resposta_inserida)}")