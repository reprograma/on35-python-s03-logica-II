#Faça um programa que receba dois numeros e mostre o maior.
#  Se por acaso, 
# os dois números forem iguais, 
# imprima a mensagem "Números iguais".
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 == numero2:
  print("Números iguais")
else:
  if numero1 > numero2:
    maior = numero1
  else:
    maior = numero2
  print(f"O maior número é {maior}.")