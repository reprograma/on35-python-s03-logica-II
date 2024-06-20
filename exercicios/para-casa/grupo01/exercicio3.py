#Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

numero= int(input("Digite um número de inteiro de 1 a 7 para saber qual o dia da semana: "))
if numero == 1:
    print("1-DOMINGO")
elif numero == 2:
    print("2-SEGUNDA")
elif numero == 3:
    print("3-TERÇA")
elif numero == 4:
    print("4-QUARTA")
elif numero == 5:
    print("5-QUINTA")
elif numero == 6:
    print("6-SEXTA") 
elif numero == 7:
    print("7-SÁBADO")
else:
    print("Número inválido!")


