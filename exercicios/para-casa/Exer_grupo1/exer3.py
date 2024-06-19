# Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

numero = int(input("Digite seu numero de 1 a 7: "))

if numero < 1 or numero > 7:
    print("Número inválido! Por favor, digite um número entre 1 e 7.")
else:
 dias_da_semana = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }
 print(f'O dia da semana {numero} é: {dias_da_semana[numero]}')