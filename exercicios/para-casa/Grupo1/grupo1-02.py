#Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".

numero1 = float(input("Primeiro número: "))
numero2 = float(input("Segundo número: "))

if numero1 > numero2: 
    print("O primeiro número é maior:", numero1)
elif numero2 > numero1: 
    print("O segundo número é maior:", numero2)
else: 
    print("Números iguais")
