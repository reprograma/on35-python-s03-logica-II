## Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".


def calculo(numero1,numero2):
    if  numero1 > numero2:
        return f"O número {numero1} é maior que o {numero2}."
    elif  numero2 > numero1:        
        return f"O número {numero2} é maior que o {numero1}."
    else: numero1 == numero2
    return "Números iguais."


numero1 = int(input("adicione o primeiro número: "))
numero2 = int(input("adicione o segundo número: "))

resposta = calculo(numero1,numero2)
print(resposta)