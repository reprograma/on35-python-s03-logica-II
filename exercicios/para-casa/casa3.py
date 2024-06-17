# Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. 
# Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

def dia_inserido(dia_da_semana):
    if dia_da_semana == 1:
        return "O dia da semana é Domingo"
    elif dia_da_semana == 2:
        return "O dia da semana é Segunda-feira"
    elif dia_da_semana == 3:
        return "O dia da semana é Terça-feira"
    elif dia_da_semana == 4:
        return "O dia da semana é Quarta-feira"
    elif dia_da_semana == 5:
        return "O dia da semana é Quinta-feira"
    elif dia_da_semana == 6:
        return "O dia da semana é Sexta-feira"
    elif dia_da_semana == 7:
        return "O dia da semana é Sábado"
    else:
        return "Número inserido diferente de 1 a 7"
    

numero_inserido = int(input('Digite um número inteiro de 1 a 7: '))
numero_correspondente = dia_inserido(numero_inserido)

print(numero_correspondente)