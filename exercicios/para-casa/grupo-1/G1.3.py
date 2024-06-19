#Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

def dias_semana (n):
    if n == '1':
        return 'Domingo'
    elif n == '2':
        return 'Segunda-feira'
    elif n == '3':
        return 'Terça-feira'
    elif n == '4':
        return 'Quarta-feira'
    elif n == '5':
        return 'Quinta-feira'
    elif n == '6':
        return 'Sexta-feira'
    elif n == '7':
        return 'Sábado'
    else:
        return 'Número inválido. Escolha um número de 1 a 7'

dia = input('Digite um número de 1 a 7 ')
resultado = print(dias_semana(dia))