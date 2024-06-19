#Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.


def numero_inteiro(numero):
    if numero == 1:
        return 'Domingo'
    elif numero == 2:
        return 'Segunda-Feira'
    elif numero == 3:
        return 'Terça-Feira'
    elif numero == 4:
        return 'Quarta-Feira'
    elif numero == 5:
        return 'Quinta-Feira'
    elif numero == 6:
        return 'Sexta-Feira'
    elif numero == 7:
        return 'Sábado-Feira'
    else:
        return 'Não entendi, digite novamente'

numero = int(input('Insira um numero da 1 a 7 correspondente ao dia da semana'))
print (numero)
dia_da_semana = numero_inteiro(numero)
print (f'O dia da semana correspondente ao numero digitado é {dia_da_semana}')   

    