# Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.

def verificar_maior( n1 , n2 ) :
    if n1 > n2 : 
        return f'O número maior é : {n1}'
    elif n2 > n1 :
        return f'O número maior é : {n2}'
 

num1 = int(input('Insira um número'))
num2 = int(input('Insira um número'))

resultado = (verificar_maior(num1,num2))
print(resultado)