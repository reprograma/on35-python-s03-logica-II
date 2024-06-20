# Exercício de Casa 🏠 

## Exercício: grupo 1

# Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.

def calcular_diferenca(num1, num2):
    try:
    
        if num1 == num2:
            print("Os números digitados são iguais!")
        elif num1 > num2:
            maior = num1
            menor = num2
        else:
            maior = num2
            menor = num1

        diferenca = maior - menor

      
        print(f"O maior número é: {maior}")
        print(f"A diferença entre {maior} e {menor} é: {diferenca}")

    except ValueError :  
        print('número inserido inválido')


num1 = 10
num2 = 5
calcular_diferenca(num1,num2)