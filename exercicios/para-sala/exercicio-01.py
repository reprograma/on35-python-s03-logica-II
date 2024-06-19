# 1. Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.

def ver_idade(idade):
    if idade >= 18:
        return "Você tem permissão por ser +18"
    else: 
        return "Você não pode acessar a página"


digitar_idade = int(input("Por favor, digite a sua idade: "))
print(ver_idade(digitar_idade))