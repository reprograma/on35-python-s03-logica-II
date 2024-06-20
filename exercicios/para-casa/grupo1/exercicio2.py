## Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".


def calculo(numero1,numero2):
    if  numero1 > numero2:
        return f"O número {numero1} é maior que o {numero2}."
    elif  numero2 > numero1:        
        return f"O número {numero2} é maior que o {numero1}."
    else: numero1 == numero2
    return "Os dois números iguais."


primeiro_numero = int(input("Insira o primeiro número: "))
segundo_numero= int(input("Insira o segundo número: "))

resposta = calculo(primeiro_numero,segundo_numero)
print(resposta)