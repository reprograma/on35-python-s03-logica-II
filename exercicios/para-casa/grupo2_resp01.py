def soma():
    num1=int(input("Digite o primeiro número: "))
    num2=int(input("Digite o segundo número: "))
    calculo_soma= num1+num2
    print(f"A soma {num1} + {num2} = {calculo_soma}")

def subtracao():
    num1=int(input("Digite o primeiro número: "))
    num2=int(input("Digite o segundo número: "))
    calculo_subtracao= num1-num2
    print(f"A subtração {num1} - {num2} = {calculo_subtracao}")

def multiplicacao():
    num1=int(input("Digite o primeiro número: "))
    num2=int(input("Digite o segundo número: "))
    calculo_multiplicacao= num1*num2
    print(f"A multiplicação {num1} x {num2} = {calculo_multiplicacao}")

def divisao():
    num1=int(input("Digite o primeiro número: "))
    num2=int(input("Digite o segundo número: "))
    calculo_divisao= num1/num2
    print(f"A divisão {num1} / {num2} = {calculo_divisao}")

def menu():
    while True:
        print("-"*20)
        print("        MENU    ")
        print("-"*20)
        print("[1] - Somar")
        print("[2] - Subtrair")
        print("[3] - Multiplicar")
        print("[4] - Dividir")

        opcao=int(input("\nInforme a opção escolhida: "))
        
        if opcao == 1:
            soma()            
        elif opcao == 2:
            subtracao()
        elif opcao == 3:
            multiplicacao()
        elif opcao == 4:
            divisao()
        else:
            print("Opção Inválida")
            menu()
menu()






