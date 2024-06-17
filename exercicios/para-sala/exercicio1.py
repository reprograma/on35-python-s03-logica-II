# Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.

def verifica_idade(idade):
    if idade >= 18:
        return 'Você é maior de idade'
    else:
        return 'Você não é maior de idade'

idade = int(input('Por favor, insira a sua idade: '))
resultado = print(verifica_idade(idade))