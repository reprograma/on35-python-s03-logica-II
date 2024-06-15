#Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, em ambos os possíveis 
# casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.


def gosta_do_nome (resposta):
    if resposta == 'sim':
        print (f"Que legal, vamos te chamar de {nome}!")
    elif resposta == 'não':
        print("Poxa vida, como podemos te chamar então?")
    else:
        print("Não entendemos, responda com sim ou não")

nome = (input("insira seu nome: "))
inserir_gosta = (input(f'{nome}, voce gosta do seu nome:' )) 
resultado = gosta_do_nome(inserir_gosta)


