# 1. Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.


def verifica_idade(idade):
    if idade >= 18:
        return 'Usuário maior de idade'
    else:
        return 'Usuário menor de idade'
    
try:
    idade_inserida = int(input("insira sua idade: "))
    resultado = verifica_idade(idade_inserida)
    print (resultado)
except ValueError:
    print('O campo de idade precisa ser preenchido com dados numericos')




