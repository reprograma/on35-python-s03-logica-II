#Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.

#Primeira Tarefa
def diferenca_maior(numero1, numero2):
    if numero1 > numero2:
        numero_maior = numero1
        diferenca = numero1 - numero2
    else:
        numero_maior = numero2
        diferenca = numero2 - numero1
    return numero_maior, diferenca
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero_maior, diferenca = diferenca_maior(numero1, numero2)
print (f"O maior número é: {numero_maior}")
print(f"A diferença entre eles é: {diferenca}")
