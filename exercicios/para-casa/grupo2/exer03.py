# * Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5, 
# mas não simultaneamente pelos dois.

def num():
    numero = int(input("Informe um número: "))

    if numero % 3 == 0:
        print("O número é divisível por 3")
    elif numero % 5 == 0:
        print("O número é divisível por 5")
    else:
        print("O número não é divisível simultaneamente pelos dois")

num()

