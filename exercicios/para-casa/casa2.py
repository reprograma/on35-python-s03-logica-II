# Faça um programa que receba dois numeros e mostre o maior. 
# Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".

def resposta (numero1, numero2):
    if numero1 > numero2:
        maior = numero1
    elif numero2 > numero1:
        maior = numero2
    else: 
        numero1 = numero2
        return "Números iguais"

    return maior
    
numero1 = int(input("Insira o primeiro número: "))
numero2 = int(input("Insira o segundo número: "))

maior = resposta(numero1, numero2)

print(f"O maior número é: {maior}") or "Números iguais"