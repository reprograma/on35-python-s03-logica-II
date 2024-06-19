# Grupo 1: Exercício 2
# Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem 
# "Números iguais"

def comparar(numero):
    if numero1 == numero2:
        return "Números iguais."
    elif numero1 > numero2:
        return f" O número maior é o {numero1}."
    else:
        return f" O número maior é o {numero2}."

numero1 = int(input("Por gentileza, digite um número inteiro: "))
numero2 = int(input("Por gentileza, digite outro número inteiro: "))
resultado = comparar(numero1 and numero2)

print(resultado)
