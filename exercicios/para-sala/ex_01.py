# 1. Faça um programa que peça para o usuário inserir uma idade e 
# mostre na tela se ele é maior de idade ou não.

idade = int (input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade")

elif idade < 18:  # porque usar elif e não o else?
    print("Menor de idade")