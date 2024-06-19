#Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".
def verifica_numero(n1,n2):
    if n1 > n2 :
        return f'O número maior é : {n1}'
    elif n2 > n1:
        return f'O número maior é : {n2}'
    else:
        return 'Números iguais'
    
num1 = int(input('Insira um número: '))
num2 = int(input('Insira um número: '))

verificar = verifica_numero(num1,num2)
resultado = print(verificar)