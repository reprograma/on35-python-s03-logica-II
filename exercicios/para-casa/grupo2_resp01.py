def soma(num1,num2):
    calculo_soma= num1+num2
    return(calculo_soma)

def subtracao(num1,num2):
    calculo_subtracao= num1-num2
    return(calculo_subtracao)

def multiplicacao(num1,num2):
    calculo_multiplicacao= num1*num2
    return(calculo_multiplicacao)

def divisao(num1,num2):
    calculo_divisao= num1//num2
    return(calculo_divisao)

def menu():
    while True:
        print("-"*20)
        print("        MENU    ")
        print("-"*20)
        print("[1] - Somar")
        print("[2] - Subtrair")
        print("[3] - Multiplicar")
        print("[4] - Dividir")
        print("[5] - Sair")

        opcao=int(input("\nInforme a opção escolhida: "))
        
        if opcao == 1:
            num1=int(input("Digite o primerio número: "))
            num2=int(input("Digite o segundo número: "))
            calculo_soma=soma(num1,num2)
            print(f"A soma {num1} + {num2} = {calculo_soma}")

        elif opcao == 2:
            num1=int(input("Digite o primerio número: "))
            num2=int(input("Digite o segundo número: "))
            calculo_subtracao=subtracao(num1,num2)
            print(f"A subtração {num1} - {num2} = {calculo_subtracao}")

        elif opcao == 3:
            num1=int(input("Digite o primerio número: "))
            num2=int(input("Digite o segundo número: "))
            calculo_multiplicacao= multiplicacao(num1,num2)
            print(f"A multiplicação {num1} * {num2} = {calculo_multiplicacao}")

        elif opcao == 4:
            num1=int(input("Digite o primerio número: "))
            num2=int(input("Digite o segundo número: "))
            calculo_divisao=divisao(num1,num2)
            print(f"A divisão {num1} / {num2} = {calculo_divisao}")
        
        elif opcao == 5:
            break
        else:
            print("Opção Inválida :( Tente novamente!")
            menu()
menu()