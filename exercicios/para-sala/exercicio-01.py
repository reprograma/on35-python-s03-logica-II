#Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.

def inserir_idade(idade):
    if idade >= 18:
        return 'Usuário MAIOR de idade'    
    elif idade: 
        return 'Usuário MENOR de idade'

idadeinserida = int(input('Insira a idade da pessoa: '))
responder = print(inserir_idade(idadeinserida))

