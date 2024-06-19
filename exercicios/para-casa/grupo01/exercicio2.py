#Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".

numero1= int(input("Digite o primeiro número: "))
numero2= int(input("Digite o segundo número: "))

if numero1 > numero2:
    print(f"O numero {numero1} é maior que o numero {numero2}. ")
if numero2 > numero1:
   print(f"O numero {numero2} é maior que o numero {numero1}. ") 
elif numero1 == numero2:
    print("Números iguais! ")