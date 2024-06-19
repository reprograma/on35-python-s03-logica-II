#Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.

numero1= int(input("Digite o primeiro número: "))
numero2= int(input("Digite o segundo número: "))

if numero1 > numero2:
    print(f"O numero {numero1} é maior que o numero {numero2}. ")
elif numero2 > numero1:
   print(f"O numero {numero2} é maior que o numero {numero1}. ") 

diferenca= numero1 - numero2
print(f"A diferença entre os números é de {diferenca}")





