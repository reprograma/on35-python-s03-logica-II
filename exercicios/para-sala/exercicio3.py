# 3. Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, em ambos 
# os possíveis casos de resposta (Sim ou Não),mostre uma mensagem de sua escolha na tela.
# Tentar corrigir o código para aceitar letras maiusculas e minusculas rs (danda) .strip().lower()

def gostar_nome(nome):

    if nome == 'sim':
        return "Quem bom que você gosta desse nome!"
    else:
        return "Ahhh!!! Que peninha!"

nome_inserido = input("Insira um nome: \n")
resposta_nome = input("Você gosta do nome que digitou? (sim/não) \n") .strip().lower()
resultado = print(gostar_nome(resposta_nome))


