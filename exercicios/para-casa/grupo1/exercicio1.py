## Exercício: grupo 1

## Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.

def calculo(numero1,numero2):
    if  numero1 > numero2:
        diferenca = numero1 - numero2
        return f"O número {numero1} é maior que o {numero2} e a diferença entre eles é de: {diferenca}"
    elif  numero2 > numero1:
        diferenca = numero2 - numero1
        return f"O número {numero2} é maior que o {numero1} e a diferença entre eles é de: {diferenca}"
    else: numero1 == numero2
    return "Os dois números são iguais e não há diferença entre eles."


numero1 = int(input("adicione o primeiro número: "))
numero2 = int(input("adicione o segundo número: "))

resposta = calculo(numero1,numero2)
print(resposta)