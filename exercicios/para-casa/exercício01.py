#Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.

def maior_e_diferenca(numero01, numero02):
    if numero01 > numero02:
        maior = numero01
        diferenca = numero01 - numero02
    else:
        maior = numero02
        diferenca = numero02 - numero01

    return maior, diferenca

numero01 = int(input("Digite o primeiro número : "))
numero02 = int(input("Digite o segundo número : "))

maior, diferenca = maior_e_diferenca(numero01, numero02)

print(f"O maior número é: {maior}")
print(f"A diferença entre os dois números é: {diferenca}")