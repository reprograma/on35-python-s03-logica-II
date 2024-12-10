# GRUPO 1: Exercício 3
#  Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, 
# domingo se 1, segunda-feira se 2, e assim por diante.

def semana(numero):
    if numero == 1:
        print ("Dia da semama correspondente ao número 1 é o domingo.")
    elif numero == 2:
        print ("Dia da semama correspondente ao número 2 é a segunda-feira.")
    elif numero == 3:
        print ("Dia da semama correspondente ao número 3 é a terça-feira.") 
    elif numero == 4:
        print ("Dia da semama correspondente ao número 4 é a quarta-feira.")
    elif numero == 5:
        print ("Dia da semama correspondente ao número 5 é a quinta-feira.")  
    elif numero == 6:
        print ("Dia da semama correspondente ao número 6 é a sexta-feira.")  
    elif numero == 7:
        print ("Dia da semama correspondente ao número 7 é o Sábado.")
    else:
        print ("Número informado, diferente do solicitado") 

dia_semana = int(input("Por gentileza, digite um número de 1 a 7.\n"))
resultado = semana(dia_semana)     
