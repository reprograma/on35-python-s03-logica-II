# Faça um programa que mostre ao usuario um menu com 4 opções de operações matemáticas 
# (as básicas, por exemplo). O usuário escolhe uma das opçõoes e o seu programa 
# então pede dois valores numéricos e realiza a operação, mostrando o resultado.

def adicao():
        num1 = float(input("Informe o primeiro número:"))
        num2 = float(input("Informe o segundo número: "))
        soma = num1 + num2
        print(f"A soma é {soma}")

def subtracao():
        num1 = float(input("Informe o primeiro número:"))
        num2 = float(input("Informe o segundo número: "))
        subtracao = num1 - num2
        print(f"A subtração é {subtracao}")

def multiplicacao():
        num1 = float(input("Informe o primeiro número:"))
        num2 = float(input("Informe o segundo número: "))
        multiplicacao = num1 * num2
        print(f"A multiplicação é {multiplicacao}")

def divisao():
        num1 = float(input("Informe o primeiro número:"))
        num2 = float(input("Informe o segundo número: "))
        divisao = num1 % num2
        print(f"A divisão é {divisao}")


def calculadora ():
    print("Escolha a operação: ")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    operacao = input("Digite a operação escolhida sendo 1, 2, 3 ou 4: ")

    if operacao in ["1", "2", "3", "4"]:
        num1 = float(input("Informe o primeiro número:"))
        num2 = float(input("Informe o segundo número: "))

        if operacao == 1:
            adicao()

        elif operacao == 2: 
            subtracao()
        
        elif operacao == 3:
            multiplicacao ()
        
        elif operacao == 4:
            if num2 != 0:
                divisao ()
    
            else:
                print("Valor não pode ser divisível por '0'! ")

    else:
        print("Escolha inválida. Por favor, tente novamente.")

calculadora ()

