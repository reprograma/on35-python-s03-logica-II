# Faça um programa que mostre ao usuario um menu com 4 opções de operações matemáticas (as básicas, por exemplo). O usuário escolhe uma das opçõoes e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado.

def menu():
    print('''
            MENU:

            [+] - Soma
            [-] - Subtração
            [*] - Multiplicação
            [/] - Divisão

    
        ''')

menu()
opcao = (input('Escolha uma opcao: '))

valor1 = int(input('Insira o primeiro valor: '))
valor2 = int(input('Insira o segundo valor: '))


if opcao == '+':
    print(f'O resultado da soma é: {valor1 + valor2}')
elif opcao == '-':
    print(f'O resultado da subtração é: {valor1 - valor2}')
elif opcao == '*':
        print(f'O resultado da multiplicação é: {valor1 * valor2}')
elif opcao == '/':
    if valor2 != 0:
        print(f'O resultado da divisão é: {valor1 / valor2}')
    else:
         print('Divisão por zero não pode ser realizada')
else:
    print('Opcao invalida')






