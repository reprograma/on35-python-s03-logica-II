# Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".
def numero_maior(numero1,numero2):
    if numero1>numero2:
      print (f'O primeiro numero inserido[{numero1}] é o maior') 
    elif numero2>numero1:
      print (f'O segundo numero inserido[{numero2}] é o maior') 
    elif numero1 == numero2:
      print (f'Os numeros são iguais') 

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero:" ))
numero_maior(numero1,numero2)
 
