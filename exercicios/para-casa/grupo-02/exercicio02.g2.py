#Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5, mas não simultaneamente pelos dois.

numero = int(input("Insira um número: "))

if numero % 5 == 0:
    print("É divisível por 5")
elif numero % 3 == 0:
    print("É divisivel por 3")
else:
    print("não é divisivel nem por 3 e nem por 5")