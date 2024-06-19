#Faça um programa que mostre ao usuario um menu com 4 opções de operações matemáticas (as básicas, por exemplo). O usuário escolhe uma das opçõoes e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado.
# Função para exibir o menu e obter a escolha do usuário
def exibir_menu():
    print("Escolha a operação desejada:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    escolha = input("Digite o número da operação desejada: ")
    return escolha

# Loop principal do programa
while True:
    opcao = exibir_menu()

    if opcao == '0':
        print("Encerrando o programa...")
        break
    elif opcao in ['1', '2', '3', '4']:
        try:
            # Captura os números inseridos pelo usuário
            valor1 = float(input("Digite o primeiro valor: "))
            valor2 = float(input("Digite o segundo valor: "))

            # Realiza a operação correspondente à escolha do usuário
            if opcao == '1':
                resultado = valor1 + valor2
                print(f"Resultado da adição: {resultado}")
            elif opcao == '2':
                resultado = valor1 - valor2
                print(f"Resultado da subtração: {resultado}")
            elif opcao == '3':
                resultado = valor1 * valor2
                print(f"Resultado da multiplicação: {resultado}")
            elif opcao == '4':
                if valor2 != 0:
                    resultado = valor1 / valor2
                    print(f"Resultado da divisão: {resultado}")
                else:
                    print("Erro: divisão por zero")
        except ValueError:
            print("Por favor, digite valores numéricos válidos.")
    else:
        print("Opção inválida. Escolha novamente.")
