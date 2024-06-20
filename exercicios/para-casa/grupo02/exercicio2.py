#Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5, mas não simultaneamente pelos dois.

def divisao(numero):
    if numero % 3==0 and numero % 5 == 0:
        return "Número inválido! Divisivel por 3 e 5 simultaneamente"
    elif numero % 3==0 or numero % 5 == 0:
        return "Número válido! Divisivel por 3 ou 5"
    else:
        return "Número inválido, não divisivel por 3 ou 5! "


numero = int(input("Insira um número inteiro: "))
print(divisao(numero))