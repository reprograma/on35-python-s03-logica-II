# Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".
numero1 = int(input("Digite seu primeiro numero: "))
numero2 = int(input("Digite seu segundo numero: "))

if numero1 > numero2:
    print(f'O maior número é: {numero1}')
elif numero2 > numero1:
     print(f'O maior número é: {numero2}')   
else:
     print("Números iguais")