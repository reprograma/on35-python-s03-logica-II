# Faça um programa que receba dois numeros e mostre o maior.
# Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))


def maior(numero1, numero2):
    if numero1 > numero2:
        maiornumero = numero1
    elif numero2 > numero1:
        maiornumero = numero2
    else:
        return "Números iguais"

    return f"O maior é o número {maiornumero}"


resultado = maior(numero1, numero2)

print(resultado)
