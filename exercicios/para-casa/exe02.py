# Exercício de Casa 🏠 

## Exercício: grupo 1

#* Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".

def maior_numero(numero1, numero2):
  
  if numero1 > numero2:
    return numero1
  elif numero1 < numero2:
    return numero2
  else:
    return "Números iguais"

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

maior = maior_numero(numero1, numero2)

if numero1 == numero2:
  print(f"Os números {numero1} e {numero2} são iguais.")
  
else:
  print(f'O numero maior é: {maior}')
