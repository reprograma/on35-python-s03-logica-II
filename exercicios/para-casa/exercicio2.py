#Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".

numero1 = int (input("Digite o primeiro numero aqui: "))
numero2 = int (input("Digite o segundo numero aqui: "))

if numero1 > numero2:
    print("O maior numero é o primeiro digitado")
elif numero1 == numero2:
    print("Números Iguais")
else: 
    print("O maior numero é o segundo digitado")
