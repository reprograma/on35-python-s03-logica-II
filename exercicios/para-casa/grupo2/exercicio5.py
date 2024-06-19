# Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5, mas não simultaneamente pelos dois.


def verifica_numero (numero):
    if (numero_inteiro % 3 and numero_inteiro % 5 != 0) or (numero_inteiro % 3 != 0 and numero % 5 == 0):
        return "Esse numero é válido"
    else:
        return "Esse numero é inválido"

numero_inteiro = int(input("Insira aqui seu numero inteiro: "))
print(verifica_numero(numero_inteiro))