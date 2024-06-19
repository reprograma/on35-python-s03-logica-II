# Faça um programa que mostre ao usuario um menu com 4 opções de operações matemáticas (as básicas, por exemplo). 
# O usuário escolhe uma das opçõoes e o seu programa então pede dois valores numéricos 
# e realiza a operação, mostrando o resultado.

def calculate():
    operation = input('''
Escolha a operação matemática que gostaria de utilizar:
+ para adição
- para subtração
* para mutiplicação
/ para divisão
''')

    numero_1 = float(input('Digite o primeiro número: '))
    numero_2 = float(input('Digite o segundo número:: '))

    if operation == '+':
        print('{} + {} = '.format( numero_1, numero_2))
        print( numero_1 + numero_2)

    elif operation == '-':
        print('{} - {} = '.format( numero_1, numero_2))
        print( numero_1 - numero_2)

    elif operation == '*':
        print('{} * {} = '.format( numero_1, numero_2))
        print( numero_1 * numero_2)

    elif operation == '/':
        print('{} / {} = '.format(numero_1, numero_2))
        print( numero_1/ numero_2)

    else:
        print('Você digitou um operador inválido, tente novamente')

    again()

def again():
    calc_again = input('''
Deseja calcular de novo?
Digite S para Sim ou N para Não.
''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('Fim!')
    else:
        again()

calculate()