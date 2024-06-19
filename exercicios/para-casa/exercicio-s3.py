# Exercício de Casa 🏠 

## Exercício: grupo 1

#Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.

try:
    numero1 = int(input("Por favor, digite um número inteiro: "))
except ValueError:
    print("Você não digitou um número inteiro válido.")

try:
    numero2 = int(input("Por favor, digite outro número inteiro: "))
except ValueError:
    print("Você não digitou um número inteiro válido.")

if numero1 > numero2:
    maior = numero1
    menor = numero2
else: 
    maior = numero2
    menor = numero1

diferença = maior - menor

print(f"O maior número é: {maior}")
print(f"A diferença entre eles é: {diferença}")


#Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".


numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))

if numero1 > numero2:
    print(f"O maior número é: {numero1}")
elif numero2 > numero1:
    print(f"O maior número é: {numero2}")
else:
    print("Números iguais")



#Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.



numero = int(input("Digite um número entre 1 e 7: "))

if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Segunda-feira")
elif numero == 3:
    print("Terça-feira")
elif numero == 4:
    print("Quarta-feira")
elif numero == 5:
    print("Quinta-feira")
elif numero == 6:
    print("Sexta-feira")
elif numero == 7:
    print("Sábado")
else:
    print("Somente números de 1 a 7. Por favor, digite um número entre 1 e 7.")



