## Exercício: grupo 1

# * Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.
# * Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".
# * Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

# Exercício 1 e 2:
def identificarmaior (num1, num2):
    if num1>num2:
        resultado1 = num1 - num2
        return f'{num1} é maior que {num2}, e a diferença entre eles é de {resultado1}'
    elif num2>num1:
        resultado2 = num2 - num1
        return f'{num2} é maior que {num1}, e a diferença entre eles é de {resultado2}'
    elif num1 == num2:
        return 'Os números são iguais'
    
num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))
print(identificarmaior(num1, num2))    

def diadasemana (numero):
    if numero == 1:
        return 'domingo'
    elif numero == 2:
        return 'segunda-feira'
    elif numero == 3:
        return 'terça-feira'
    elif numero == 4:
        return 'quarta-feira'
    elif numero == 5:
        return 'quinta-feira'
    elif numero == 6:
        return 'sexta-feira'
    elif numero == 7:
        return 'sábado'
    else:
        return 'Você não inseriu um número válido'
    
numero = int(input('Por favor, insira um número: '))
print(diadasemana(numero))


