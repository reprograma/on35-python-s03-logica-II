#Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".

numero1 = int (input("Digite o primeiro numero aqui: "))
numero2 = int (input("Digite o segundo numero aqui: "))

if numero1 > numero2:
    print(f"O maior numero é o {numero1}")
elif numero1 == numero2:
    print("Números Iguais")
else: 
    print(f"O maior numero é o {numero2}")
