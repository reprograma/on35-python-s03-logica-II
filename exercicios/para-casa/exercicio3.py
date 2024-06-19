#Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

numero = int(input("Escolha um número entre 1 e 7"  ))
if numero == 1:
    print("Segunda-feira")
elif numero == 2:
    print("Terça-feira")
elif numero == 3:
    print("Quarta-feira")
elif numero == 4:
    print("Quinta-feira")
elif numero == 5:
    print("Sexta-feira")
elif numero == 6:
    print("Sábado")
elif numero == 7:
    print("Domingo")
else: 
    print("Este dia não existe.")

