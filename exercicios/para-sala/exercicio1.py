# 1. Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.

try:

    def verifica_idade(idade):
        if idade >= 18:
            return "Você é maior de idade."
        else:
            return "Você é menor de idade"  

    idade_inserida = int(input('Por gentileza, digite uma idade: '))
    resultado = print(verifica_idade(idade_inserida))
except ValueError:
       print("Número inserido, inválido.")   
