# Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))


def maior_numero(numero1, numero2):
    if numero1 > numero2:
        diferenca = numero1 - numero2
        return f"O maior é o {numero1}. A diferença é igual a {diferenca}"
    elif numero2 > numero1:
        diferenca = numero2 - numero1
        return f"O maior é o {numero2}. A diferença é igual a {diferenca}"
    else:
        return "Os números são iguais. Não há diferença."


resposta = maior_numero(numero1, numero2)

print(resposta)
