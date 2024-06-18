# Faça um programa que mostre na tela uma pergunta de múltipla escolha, e que, a partir da resposta do usuário, mostre na tela se ele acertou ou não.


def verifica_resposta (resposta):
    if resposta == 42:
        return 'Uhuul! Você acertou!!'
    else:
        return 'Você errou! =('
    
resposta = int(input('Qual a resposta para a vida, o universo e tudo mais?\n a)35 b)42 c)1000000000 d)3698\n Digite sua resposta:'))
resultado = print(verifica_resposta(resposta))