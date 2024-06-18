# Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, 
# pergunte quantos e mostre na tela uma mensagem de sua escolha. No caso de o usuário responder “não”, 
# pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.
# 

def tem_irmaos(resposta):
    if resposta == 'sim':
        input('Que legal! Quantos irmãos você tem? ')
    else: 
        respostadois= input('Você gostaria de ter irmãos? ')
        if respostadois == 'sim':
                print('Que bom! Ter irmãos é super legal')
        else: 
                print('Entendo. Ter irmão às vezes é complicado')
    

resposta = input('Você tem irmaos? ')
print(tem_irmaos(resposta))



