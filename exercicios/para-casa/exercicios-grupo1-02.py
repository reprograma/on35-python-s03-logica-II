
# * Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".


def calculo(numero1,numero2):
    if numero1 > numero2:
        return f"Número maior = {numero1}"
    elif numero2 > numero1:
        return f"Número maior = {numero2}"
    else:
        return f"Números iguais"


numero1 = float(int(input("Escolha um número: ")))
numero2 = float(int(input("Escolha mais um número: ")))

resultado = calculo(numero1,numero2)
print(resultado)

