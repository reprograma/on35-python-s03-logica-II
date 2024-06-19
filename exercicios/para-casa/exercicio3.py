# Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.


def dias_da_semana(escolha):
    
    if escolha == 1:
        return("Segunda-feira")
    elif escolha == 2:
        return("Terça-feira")
    elif escolha == 3:
        return("Quarta-feira")
    elif escolha == 4:
        return("Quinta-feira")
    elif escolha == 5:
        return("Sexta-feira")
    elif escolha == 6:
        return("Sábado")
    elif escolha == 7:
        return("Domingo")
    else:
        return("Número inválido")
    

numero_correspondente = int(input("Indique um numero entre 1 e 7 para dia da semana correspondente: "))
resultado = dias_da_semana(numero_correspondente)
print(resultado)