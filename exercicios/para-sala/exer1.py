#1. Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.


try:
    idade = int(input('Insira sua idade: '))
    
    if idade >= 18:
        print('Você é maior de idade ')
    else:
        print('Você é menor de idade ')

except ValueError:
    print('Por favor, insira um número inteiro válido para a idade.')