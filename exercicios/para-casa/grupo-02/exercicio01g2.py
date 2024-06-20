#Faça um programa que mostre ao usuario um menu com 4 opções de operações matemáticas (as básicas, por exemplo). 
#O usuário escolhe uma das opçõoes e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado.

operação = input("Qual operação você deseja realizar? \n + Adição\n - Subtração\n / Divisão\n * Multiplicação\nEscolha um símbolo ou escreva a palavra: ")

numero1 = float(input("Insira um numero: "))
numero2 = float(input("insira outro número: "))

if operação == '+' or operação.lower() == "Adição":
    print(numero1 + numero2)
elif operação == '-' or operação.lower() == "Subtração":
    print(numero1 - numero2)
elif operação == '/' or operação.lower() == "Divisão":
    print(numero1 / numero2)
elif operação == '*' or operação.lower() == "Multiplicação":
    print(numero1 * numero2)
else:
    print("Resposta inválida")