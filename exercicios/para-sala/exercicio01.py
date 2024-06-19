#1. Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.

def qual_idade(idade):
    if idade >= 18:
        return 'Você é maior de idade.'
    elif idade == 17:
        return 'Falta pouco, mas ainda não!'
    else:
        return 'Você NÃO é maior de idade!'
    
idade_informada = int(input('Insira a sua idade: '))
resultado = qual_idade(idade_informada)

print(resultado)