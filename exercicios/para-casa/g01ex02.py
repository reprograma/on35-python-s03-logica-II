# Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".

def numeros (n1, n2):
    if n1 > n2:
        print(f"Pelo visto, {n1} é maior")
    elif n2 > n1:
        print(f"Pelo visto, {n2} é maior")
    elif n1 == n2:
        print(f"Ambos os números são iguais")
    
numero1 = int(input("Insira o primeiro número: "))
numero2 = int(input("Insira o segundo número: "))

resultado = numeros(numero1, numero2)



