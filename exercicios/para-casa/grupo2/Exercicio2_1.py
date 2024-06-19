#Faça um programa que mostre ao usuario um menu com 4 opções de operações matemáticas (as básicas, por exemplo). O usuário escolhe uma das opçõoes e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado.


def opcoes(resposta):
    if resposta == 1:
        operacao1 = float(input('Insira o primeiro numero'))
        operacao2 = float(input('Insira o segundo numero')) 
        resposta = operacao1 + operacao2
        return resposta
    if resposta == 2:
        operacao1 = float(input('Insira o primeiro numero'))
        operacao2 = float(input('Insira o segundo numero')) 
        resposta = operacao1 * operacao2
        return resposta
    if resposta == 3:
        operacao1 = float(input('Insira o primeiro numero'))
        operacao2 = float(input('Insira o segundo numero')) 
        resposta = operacao1 // operacao2
        return resposta
    if resposta == 4:
        operacao1 = float(input('Insira o primeiro numero'))
        operacao2 = float(input('Insira o segundo numero')) 
        resposta = operacao1 - operacao2
        return resposta

pergunta = ('Escolha uma operação \n 1- Soma \n 2 - Multiplicação \n 3 - Divisão \n 4 - Subtração')
print(pergunta)
resposta = int(input('Insira aqui o numero da opção escolhida'))

resultado = opcoes(resposta)

print (f'O resultado da operação é igual a {resultado}')




