#Faça um programa que mostre na tela uma pergunta de múltipla escolha, e que, a partir da resposta do usuário, mostre na tela se ele acertou ou não.

def resposta_pergunta(Resposta):
    try:
        if Resposta == 1:
            print('ERROU!!!!')
        elif Resposta == 2:
            print('ACERTOU!!!!!')
        else:
            print('Número inválido')
    except:
        print('Entrada inválida. Digite um número válido.')

pergunta = 'Como está o dia hoje? \n 1- Chuvoso \n 2- Ensolarado'
print(pergunta)

try:
    Resposta = int(input('Insira o número da resposta: '))
    resposta_pergunta(Resposta)
except:
    print('Entrada inválida. Digite um número válido.')
 