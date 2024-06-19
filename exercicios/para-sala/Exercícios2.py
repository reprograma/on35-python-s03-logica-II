#Faça um programa que mostre na tela uma pergunta de múltipla escolha, e que, a partir da resposta do usuário, mostre na tela se ele acertou ou não.

def resposta_pergunta(Resposta):
    if Resposta == 1 or Resposta == 'Chuvoso'.lower():
        print ('ERROU!!!!')
    elif Resposta == 2 or Resposta == 'Ensolarado'.lower():
        print ('ACERTOU!!!!!')
    else: 
        print('Não emtendi, digite novamente')

Pergunta = 'Como está o dia hoje? \n 1- Chuvoso  \n 2- Ensolarado'
print(Pergunta)
Resposta = int(input('Insira o número da resposta.'))

resposta_pergunta(Resposta)






