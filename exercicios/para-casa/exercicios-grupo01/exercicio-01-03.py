# Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

def dias_semana(resposta):
    if resposta == '1':
        return 'Domingo'
    elif resposta == '2':
        return 'Segunda-feira'
    elif resposta == '3':
        return 'Terça-feira'
    elif resposta == '4':
        return 'Quarta-feira'
    elif resposta == '5':
        return  'Quinta-feira'
    elif resposta == '6':
        return 'Sexta-feira'
    elif resposta == '7':
        return  'Sabado'
    else:
        return 'Opção Invalida'
    
dia_escolhido = input('Digite um numero de 1 a 7: ')
resposta_elaborada = print(f'O numero {dia_escolhido} corresponde ao dia da semana {dias_semana(dia_escolhido)}')