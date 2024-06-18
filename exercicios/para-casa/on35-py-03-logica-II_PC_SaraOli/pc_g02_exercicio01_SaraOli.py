# * Faça um programa que mostre ao usuario um menu com 4 opções de operações matemáticas (as básicas, por exemplo). 
# • O usuário escolhe uma das opçõoes
# • O programa então pede dois valores numéricos
# • Realiza a operação, mostrando o resultado.

# - Conjunto de funções que realizam as operações matemáticas
def conta_de_mais(a, b):
    return a + b

def conta_de_menos(a, b):
    return a - b

def conta_de_dividir(a, b):
    return a / b

def conta_de_vezes(a, b):
    return a * b

def conta_de_exponencial(a, b):
    return a ** b

# - Função calculadora, realiza as operações a partir da entrada de dados da pessoa usuária.
def calculadora():
    
    # - While booleano que "printa" na tela as operações disponíveis para a pessoa usuária. Ele faz o loop nos operadores lógicos até que a pessoa usuária digite "Sair" e este é o ponto de encerramento do programa.
    while True:
        print('Bem-vinde ao Calcularôta!\nEscolha a operação desejada:\nDigite: + para Adição\nDigite: - para Subtração\nDigite: / para Divisão\nDigite: * para Multiplicação\nDigite: ** para Exponenciação\nDigite: Sair para encerrar a Calcularôta')
        
        escolhaOperacao = input('Escolha a operação desejada: ').lower()

        if escolhaOperacao == 'sair':
            print('Saindo da Calcularôta, até a próxima!')
            break
        else:
            primeiroValor = float(input('Digite o primeiro número: '))
            segundoValor = float(input('Digite o segundo número: '))
            if escolhaOperacao == '+':
                resultado_adicao = conta_de_mais(primeiroValor, segundoValor)
                print(f"O resultado da operação é: {resultado_adicao}")
            elif escolhaOperacao == '-':
                resultado_adicao = conta_de_menos(primeiroValor, segundoValor)
                print(f"O resultado da operação é: {resultado_adicao}")
            elif escolhaOperacao == '/':
                resultado_adicao = conta_de_dividir(primeiroValor, segundoValor)
                print(f"O resultado da operação é: {resultado_adicao}")
            elif escolhaOperacao == '*':
                resultado_adicao = conta_de_vezes(primeiroValor, segundoValor)
                print(f"O resultado da operação é: {resultado_adicao}")
            elif escolhaOperacao == '**':
                resultado_adicao = conta_de_exponencial(primeiroValor, segundoValor)
                print(f"O resultado da operação é: {resultado_adicao}")
            else:
                print("Entrada inválida, por favor, tente novamente.")

calculadora()
