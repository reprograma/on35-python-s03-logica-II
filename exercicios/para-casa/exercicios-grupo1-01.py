
# * Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.


def calculo(numero1,numero2):
    if numero1 > numero2:
       divisao1 = numero1 - numero2
       return f"Número maior = {numero1}. Divisão entre ambos ={divisao1}"
    elif numero2 > numero1:
        divisao2 = numero2 - numero1
        return f"Número maior = {numero2}. Divisão entre ambos ={divisao2}"
    else: 
        return f"Número inválido."
    

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado = calculo(numero1,numero2)
print(resultado)