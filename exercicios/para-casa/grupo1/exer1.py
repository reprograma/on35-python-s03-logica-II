# Escreva um programa que, dados dois numeros inteiros, 
# mostre na tela o maior deles, 
# assim como a diferença existente entre ambos.

def mostre_numeros():
    num1 = int(input("Informe um número1? : "))
    num2 = int(input("Informe um número2? : "))

    if num1 > num2:
        maior = num1
        diferenca = num1 - num2
        
    else:
        maior = num2
        diferenca = num2 - num1

    return maior, diferenca
    
maior, diferenca = mostre_numeros()
print(f"O maior número entre os dois é {maior} e a diferença entre eles é {diferenca}.")


