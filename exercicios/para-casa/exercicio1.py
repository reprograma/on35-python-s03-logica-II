#Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.
numero_1 = int(input("Informe o número 1 "))
print (numero_1)

numero_2 = int(input ("Informe o número 2 "))
print (numero_2)

if numero_1 > numero_2:
    print("O maior número é", numero_1)
    print (numero_1-numero_2)
else:
    print("O maior número é", numero_2) 
    print (numero_2-numero_1)

