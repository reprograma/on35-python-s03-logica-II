# Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.

numero1 = int(input("Digite seu primeiro numero de 1 a 7: "))
numero2 = int(input("Digite seu segundo numero de 1 a 7: "))

if numero1 > numero2:
    maior = numero1
    menor = numero2
else:
    maior = numero2
    menor = numero1

diferenca = maior - menor

print(f"O maior número é: {maior}")
print(f"A diferença entre eles é: {diferenca}")