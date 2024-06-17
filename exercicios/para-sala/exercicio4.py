# Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, 
# pergunte quantos e mostre na tela uma mensagem de sua escolha. No caso de o usuário responder “não”, 
# pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.
# def tem_irmaos(resposta):
#     if resposta == 'sim':
#         return input('Quantos irmãos você tem? ')
#     else: 
#         return input('Você gostaria de ter irmãos? ')
    


# respostaInserida = input('Você tem irmaos? ')

resposta = input('Você tem irmaos? ')

if resposta == 'Sim':
    resposta_positiva = input ('Que legal! Quantos irmãos você tem?')
    sua_resposta = f'Você tem {resposta_positiva} irmãos'
    print(sua_resposta)
else:
    resposta_negativa= input('Que pena! Você gostaria de ter?')
    sua_resposta_neg = f"Obrigada por sua resposta!"
    print(sua_resposta_neg)


