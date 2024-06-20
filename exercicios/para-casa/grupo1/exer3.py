# Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. 
# Isto é, domingo se 1, segunda-feira se 2, e assim por diante.


def dia_da_semana():
    dia = int(input("Escolha um número de 1 a 7 para descobrir o dia da semana: "))
    
    if dia == 1:
        return "Segunda"
    elif dia == 2:
        return "Terça"
    elif dia == 3:
        return "Quarta"
    elif dia == 4:
        return "Quinta"
    elif dia == 5:
        return "Sexta"
    elif dia == 6:
        return "Sábado"
    elif dia == 7:
        return "Domingo"
    else:
        return "Dia não encontrado"

print(dia_da_semana())
        