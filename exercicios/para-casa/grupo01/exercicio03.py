#Escreva um programa que leia um inteiro entre 1 e 7
#  e imprima o dia da semana correspondente a este número. 
# Isto é, domingo se 1, segunda-feira se 2, e assim por diante.
numero_digitado = int(input("Digite um número entre 1 e 7: "))
if numero_digitado == 1:
  print("Domingo")
elif numero_digitado == 2:
  print("Segunda-feira")
elif numero_digitado == 3:
  print("Terça-feira")
elif numero_digitado == 4:
  print("Quarta-feira")
elif numero_digitado == 5:
  print("Quinta-feira")
elif numero_digitado == 6:
  print("Sexta-feira")
elif numero_digitado == 7:
  print("Sábado")
else:
  print("Número inválido")
  