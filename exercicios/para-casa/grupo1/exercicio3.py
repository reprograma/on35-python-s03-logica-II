# Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.


def dias_semana (dia):
    if dia == int ("1"):
        return ("Esse dia corresponde a Domingo")
    elif dia == int ("2"):
        return ("Esse dia corresponde a Segunda")
    elif dia == int ("3"):
        return ("Esse dia corresponde a Terça-feira")
    elif dia == int ("4"):
        return ("Esse dia corresponde a Quarta-feira")
    elif dia == int ("5"):
        return ("Esse dia corresponde a Quinta-feira")
    elif dia == int ("6"):
        return ("Esse dia corresponde a Sexta-feira")
    elif dia == int ("7"):
        return ("Esse dia corresponde a Sabado")
    else:
        return("Digite novamente escolhendo opções entre 1 e 7")
    
try:
    dia_escolhido = int(input("Considerando que \n 1 Domingo \n 2 Segunda-feira \n 3 Terça-feira \n 4 Quarta-feira \n 5 Quinta-feira \n 6 Sexta-feira \n 7 Sabado \n Insira o código do dia da semana que deseja visualizar:  "))

    print (dias_semana(dia_escolhido))
except ValueError:
    print ('Campo incorreto, digite novamente escolhendo opções entre 1 e 7')
