# Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.
def define_maior(num1,num2):
    if num1 == num2:
        print('Os numeros sao iguais!')
    elif num1 > num2:
        print (f"Primeiro numero inserido= {num1}. Segundo numero inserido= {num2}. Maior Numero: {num1}")
        diferenca = num1-num2
        print (f"Diferença entre os numeros: {diferenca}")
    else:
        print (f"Primeiro numero inserido= {num1}. Segundo numero inserido= {num2}. Maior Numero: {num2}")
        diferenca = num2-num1
        print (f"Diferença entre os numeros: {diferenca}")

try:
    num1 = int(input('Digite um numero inteiro: '))
    num2 = int(input('Digite um segundo numero: '))
    define_maior(num1,num2)
except ValueError:
    print('Favor inserir apenas numeros inteiros!')