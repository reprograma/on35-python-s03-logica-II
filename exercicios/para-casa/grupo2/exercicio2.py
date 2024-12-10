
## Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5, mas não simultaneamente pelos dois.


def divisão(numero):
    
    if (numero % 3 == 0) ^ (numero % 5 == 0):
        return f"O número {numero} é divisivél por 3 ou 5, mas não simutaneamente pelo os dois."
    else:
        return f"O número {numero} não atende os critérios"


numero_inserido = int(input("insira um número inteiro: "))
print(divisão(numero_inserido))