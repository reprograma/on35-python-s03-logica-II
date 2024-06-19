# Grupo 1: Exercício 1
# Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.

def comparar(numero):
    if numero1 == numero2:
        return "Números iguais, logo a diferença entre eles é 0."
    elif numero1 > numero2:
        return f"Número {numero1} maior que o número {numero2} e a diferença entre os números é {numero1 - numero2}."
    else:
        return f"Número {numero2} é maior que o número {numero1} e a diferença entre os números é {numero2 - numero1}."

numero1 = int(input("Por gentileza, digite um número inteiro: "))
numero2 = int(input("Por gentileza, digite outro número inteiro: "))
resultado = comparar(numero1 and numero2)

print(resultado)
