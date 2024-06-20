# Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

dia_semana = input("Digite um número de 1 a 7 \n 1 \n 2 \n 3\n 4\n 5\n 6\n 7\nEscolha uma das alternativas: ")

if dia_semana == '1' :
    print('Domingo')
elif dia_semana == '2' :
    print('Segunda-feira')
elif dia_semana == '3' :
    print('Terça-feira')
elif dia_semana == '4' :
    print('Quarta-feira')
elif dia_semana == '5' :
    print('Quinta-feira')
elif dia_semana == '6' :
    print('Sexta-feira')
elif dia_semana == '7' :
    print('Sábado')
else:
    print("Resposta inválida")