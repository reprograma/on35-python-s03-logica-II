#Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem 
#"Números iguais".

numero1 = int(input("digite o numero1: "))
numero2 = int(input("digite o numero2: "))

if numero1 > numero2:
    print("numero1 e maior que numero2")

elif numero2 > numero1:
    print("numero2 e maior que numero1")

else:
    print("numeros iguais")


