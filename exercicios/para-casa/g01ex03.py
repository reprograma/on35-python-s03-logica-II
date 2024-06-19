# Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

def semana (dia):
    if dia == 1:
        return "Domingo"
    elif dia == 2:
        return "Segunda-Feira"
    elif dia == 3:
        return "Terça-Feira"
    elif dia == 4:
        return "Quarta-Feira"
    elif dia == 5:
        return "Quinta-Feira"
    elif dia == 6:
        return "Sexta-Feira"
    elif dia == 7:
        return "Sábado"
    else:
        return "inválido"
    
    
pergunta = int(input("Escolha um dia da semana sendo: 1/Domingo 2/Segunda-Feira 3/Terça-Feira 4/Quarta-Feira 5/Quinta-Feira 6/Sexta-Feira 7/Sábado "))

print(semana(pergunta))


