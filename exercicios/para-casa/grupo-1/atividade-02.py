# Faça um programa que receba dois numeros e mostre o maior. 
# Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".

numero1 = float(input("Informe o primeiro número:"))
numero2 = float(input("Informe o segundo número:"))

if numero1 > numero2:
    print(f" O maior número é: {numero1}")

elif numero2 > numero1:
    print(f"O maior número é: {numero2}")

else:
    print("Númros Iguais")