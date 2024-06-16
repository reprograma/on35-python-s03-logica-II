# Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

Domingo = int (1)
Segunda_feira = int (2)
Terça_feira = int (3)
Quarta_feira = int (4)
Quinta_Feira = int (5)
Sexta_feira = int (6)
Sabado = int (7)

dia_escolhido = input("insira o código do dia da semana que deseja visualizar: ") 

if dia_escolhido == Domingo:
    print ('O dia selecionado foi Domingo')
elif dia_escolhido == Segunda_feira:
    print ('O dia selecionado foi Segunda-Feira')
elif dia_escolhido == Terça_feira:
    print ('O dia selecionado foi Terça-Feira')
elif dia_escolhido == Quarta_feira:
    print ('O dia selecionado foi Quarta-Feira')
elif dia_escolhido == Quinta_Feira:
    print ('O dia selecionado foi Quinta-Feira')
elif dia_escolhido == Sexta_feira:
    print ('O dia selecionado foi Sexta-Feira')
elif dia_escolhido == Sabado:
    print ('O dia selecionado foi Sabado')
else:
    print ('Escolha uma opção de 1 - 7 válida')

print(dia_escolhido)
