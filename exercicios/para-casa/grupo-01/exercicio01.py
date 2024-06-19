#Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.

def maior(numero1,numero2):
    if numero1 > numero2:
        print(numero1)
        print(numero1-numero2)
    else: 
        print(numero2)
        print(numero2-numero1)
    
numero1 = int(input('Insira um numero: '))
numero2 = int(input('Insira outro numero: '))

maior(numero1,numero2)



