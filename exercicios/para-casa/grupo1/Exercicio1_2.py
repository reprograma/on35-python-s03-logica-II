#Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".

def numeros(x,y):
    if x > y:
        diferenca = x - y 
        return (f'O número maior é o {x} e a diferença entre o {x} e o {y} é gual a {diferenca}')
    elif y > x:
        diferenca = y - x
        return (f'O número maior é o {y} e a diferença entre o {y} e o {x} é gual a {diferenca}')
    else: 
        return ('números iguais')
     
x = int(input('Insira o primeiro número:'" "))
y = int(input('Insira o segundo número:'" "))

resultado_numeros = numeros(x,y)
print (resultado_numeros)