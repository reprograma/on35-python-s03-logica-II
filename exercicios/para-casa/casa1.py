# Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, 
# assim como a diferença existente entre ambos.


def resposta (numero1, numero2):
    if numero1 > numero2:
        maior = numero1
        diferenca = numero1 - numero2
    elif numero2 > numero1:
        maior = numero2
        diferenca = numero2 - numero1
    else: 
     diferenca = 0

    return maior, diferenca
    
numero1 = int(input("Insira o primeiro número: "))
numero2 = int(input("Insira o segundo número: "))

maior, diferenca = resposta(numero1, numero2)

print(f"O maior número é: {maior}")
print(f"A diferença entre eles é: {diferenca}")

