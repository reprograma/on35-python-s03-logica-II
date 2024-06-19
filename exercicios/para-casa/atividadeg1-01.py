# Exercício de Casa 🏠 Grupo 1
##Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.

def maior_numero_inteiro():
    numero1 = int(input("Digite o numero1: "))
    numero2 = int(input("Digite o numero2: "))

    if numero1 > numero2:
        maior = numero1
        diferenca = numero1 - numero2
        print(f"O maior número é {maior}")
    elif numero1 < numero2:
        maior = numero2
        diferenca = numero2 - numero1
        print(f"O maior número é {maior}")
    else:
        print("numero1 e numero2 são iguais")
        return

    print(f"A diferença entre os números é {diferenca}")

# Chamando a função para executar
maior_numero_inteiro()
