#Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.

def comparacao_entre_numeros():
    numero1 = int(input("Insira um numero aqui: "))
    numero2 = int(input("Insira um numero aqui: "))

    if numero1 > numero2:
        diferenca = numero1 - numero2 
        print(f"{numero1} é o número maior. A diferença entre os números é {diferenca}.")
    elif numero2 > numero1:
        diferenca = numero2 - numero1
        print(f"{numero2} é o número maior. A diferença entre os números é {diferenca}.")
    else:
        print("Números iguais")
        
comparacao_entre_numeros()

