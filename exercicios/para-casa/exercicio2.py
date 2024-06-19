#Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".

numero1 = int(input("Insira um numero aqui: "))
numero2 = int(input("Insira um numero aqui: "))

if numero1 > numero2:
    print(f"{numero1} é o número maior")
elif numero2 > numero1:
    print(f"{numero2} é o número maior")
else:
    print("Números iguais")

