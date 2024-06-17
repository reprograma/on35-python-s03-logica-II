# tem que ser divisivel por 3 ou por 5 mas não pelo dois ao mesmo tempo, exemplo:numero 15 divide pelos 2.
# retornar se o numero é valido.
#Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.

numero1 = int (input("Digite o primeiro numero aqui: "))
numero2 = int (input("Digite o segundo numero aqui: "))

if numero1 > numero2:
    print(f"O maior numero é o {numero1}")
else: 
    print(f"O maior numero é o {numero2}")

diferença = (numero1 - numero2)

print(f'A diferença entre eles é de {diferença}')