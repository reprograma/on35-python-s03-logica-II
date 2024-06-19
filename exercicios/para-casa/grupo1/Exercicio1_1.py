#Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.

def numeros(x,y):
    if x > y:
        diferenca = x - y 
        return (f'O número maior é o {x} e a diferença entre o {x} e o {y} é gual a {diferenca}')
    elif y > x:
        diferenca = y - x
        return (f'O número maior é o {y} e a diferença entre o {y} e o {x} é gual a {diferenca}')
     
x = int(input('Insira o primeiro número:'" "))
y = int(input('Insira o segundo número:'" "))

resultado_numeros = numeros(x,y)
print (resultado_numeros)