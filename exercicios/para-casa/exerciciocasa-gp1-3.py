#Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. 
#Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

#Terceira Tarefa
def semana(numero):
    if numero == 1:
        return "Domingo"
    elif numero == 2:
        return "Segunda-feira"
    elif numero == 3:
        return "Terça-feira"
    elif numero == 4:
        return "Quarta-feira"
    elif numero == 5: 
        return "Quinta-feira"
    elif numero == 6:
        return "Sexta-feira"
    elif numero == 7:
        return "Sábado"
    else:
        return "Favor digitar de 1 até 7"

numero = int(input("Digitar número entre 1 e 7: "))
dia = semana(numero)
print(dia)