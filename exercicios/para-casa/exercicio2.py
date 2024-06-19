#Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".
numero_1 = int(input("Informe o número" ))

numero_2 = int(input("Informe o número" ))

if numero_1 > numero_2:
    print("O maior número é", numero_1)
elif numero_1 == numero_2:
    print("Números iguais")
else:
    print("O maior número é", numero_2) 


