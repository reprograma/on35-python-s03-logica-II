# 1. Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.

try:
   
    idade = int(input("Informe a sua idade: "))
    
    
    if idade >= 18:
        print("Maior de idade, pode passar.")
    else:
        print("Menor de idade. Seus pais serão avisados!")
except ValueError:
  
    print(" Idade inválida. Por favor, insira um número válido para a idade.")

