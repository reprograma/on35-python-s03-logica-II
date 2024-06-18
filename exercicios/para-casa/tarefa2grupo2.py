# Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5, mas não simultaneamente pelos dois.

numero_informado = int(input("Informe o número a ser verificado: "))


def verifica_numero(numero):
    if numero_informado % 3 == 0 and numero_informado % 5 == 0:
        return "Número inválido!"
    elif numero_informado % 3 == 0:
        return "Este número é divisível por 3"
    elif numero_informado % 5 == 0:
        return "Este número é divisível por 5"
    else:
        return "Número não divisível por 3 ou 5"


resultado = verifica_numero(numero_informado)

print(resultado)
