#Faça um programa que mostre ao usuario um menu com 4 opções de operações matemáticas (as básicas, por exemplo). 
# O usuário escolhe uma das opçõoes e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado.

numero1 = int (input("Digite o primeiro numero aqui: "))
numero2 = int (input("Digite o segundo numero aqui: "))
calculo = (input("Digite a operação matematica que você deseja executar, considerando: \n + realiza adição \n - realiza subtração \n / realiza divisão \n * realiza multiplicação. \n Escolha a operação matemática:  "))

if calculo == "+":
    print (f"O resultado é {numero1+numero2}")
if calculo == "-":
    print (f"O resultado é {numero1-numero2}")
if calculo == "/":
    print (f"O resultado é {numero1/numero2}")
if calculo == "*":
    print (f"O resultado é {numero1*numero2}")
else:
    print ("Resultado invalido")


