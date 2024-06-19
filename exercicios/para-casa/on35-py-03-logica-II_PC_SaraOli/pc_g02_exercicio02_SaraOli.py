# • Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5, mas não simultaneamente pelos dois.

def divisores(numero):
    divisivelPorTres = numero % 3 == 0
    divisivelPorCinco = numero % 5 == 0

    if divisivelPorTres and divisivelPorCinco:
        return f"Este programa não está autorizado a responder a essa consulta, tente novamente com outro número!"
    if divisivelPorTres:
        return f"O {numero} é divisível por 3"
    elif divisivelPorCinco:
        return f"O {numero} é divisível por 5"
    else:
        return f"O número {numero} não é divisível por 3 ou 5."

        
numero = int(input('Insira um ou mais números e verifique se ele é divisível por 3 ou 5: '))
resultado = divisores(numero)

print(resultado)
