#Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".


def maior(numero1,numero2):
    if numero1 > numero2:
        print(numero1)
    elif numero1 == numero2:
        print('Números iguais')
    else: 
        print(numero2)
    
numero1 = int(input('Insira um numero: '))
numero2 = int(input('Insira outro numero: '))

maior(numero1,numero2)