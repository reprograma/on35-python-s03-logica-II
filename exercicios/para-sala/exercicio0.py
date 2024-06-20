#Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.

idade = int(input("insira sua idade:"))

if idade >= 18:
    print("Acesso liberado")

elif idade == 17:
    print ("Volte em breve")

else: 
    print ("acesso negado")