#Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".

def maior_ou_igual(numero01, numero02):
    if numero01 > numero02:
        return numero01

    elif numero01 < numero02:
        return numero02

    elif numero01 == numero02:

        return "Números Iguais"

numero01 = int(input("Digite o primeiro número : "))
numero02 = int(input("Digite o segundo número : "))

resultado = maior_ou_igual(numero01, numero02) 

print (resultado)
