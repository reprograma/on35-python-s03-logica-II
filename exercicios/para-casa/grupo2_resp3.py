
def divisivel_0(numero):

    return numero % 3 == 0 and numero % 5 == 0

def divisivel_diferente_0(numero):

    return numero % 3 != 0 and numero % 5 != 0

def divisivel_3(numero):

    return numero % 3 == 0 

def divisivel_5(numero):

    return numero % 5 == 0 

num=int(input("\nInforme um número inteiro: "))

if divisivel_0(num):
    print(f"{num} é divisível por 3 e 5 ao mesmo tempo")
elif divisivel_diferente_0(num):
    print(f"{num} não é divisível por 3 e 5 ao mesmo tempo")
else:
    if divisivel_3(num):
        print(f"{num} é divisível por 3")
    else:
        print(f"{num} é divisível por 5")
