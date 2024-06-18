# Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número.
# Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

numero_inteiro = int(input("Digite um número entre 1 e 7: "))


def dia_semana(numero):
    if numero_inteiro == 1:
        return "Domingo"
    elif numero_inteiro == 2:
        return "Segunda-Feira"
    elif numero_inteiro == 3:
        return "Terça-Feira"
    elif numero_inteiro == 4:
        return "Quarta-Feira"
    elif numero_inteiro == 5:
        return "Quinta-Feira"
    elif numero_inteiro == 6:
        return "Sexta-Feira"
    elif numero_inteiro == 7:
        return "Sábado"
    else:
        return "Número inválido!"


dias = dia_semana(numero_inteiro)

print(dias)
