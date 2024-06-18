# * Faça um programa que mostre ao usuario um menu com 4 opções de operações matemáticas (as básicas, por exemplo). 
# O usuário escolhe uma das opçõoes e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado.

def calculadora (operacao):
    if operacao == 'soma':
        soma = parametro1 + parametro2
        return soma
    elif operacao == 'subtração':
        subtracao = parametro1 - parametro2
        return subtracao
    elif operacao == 'multiplicação':
        multiplicacao = parametro1 * parametro2
        return multiplicacao
    elif operacao == 'divisão':
        divisao = parametro1 / parametro2
        return divisao
    else:
        print ('Desculpe! Essa não é uma operação válida')



operacao = input ('Escolha qual operação matémática você deseja realizar, entre:\na)soma\nb)subtração\nc)multiplicação\nd)divisão\n: ')
parametro1 =  int(input('Escolha o primeiro número: '))
parametro2 = int(input('Escolha o segundo número número: '))
print(calculadora(operacao))
