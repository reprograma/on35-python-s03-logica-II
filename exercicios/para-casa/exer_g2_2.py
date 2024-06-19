# Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5, 
# mas não simultaneamente pelos dois.

def divisao (numero):

    if (numero % 3 == 0 and numero % 5 == 0):
        return "Número válido, divisível por 3 e por 5."
    
    elif (numero % 3 != 0 and numero % 5 != 0):
        return "Número inválido, não sendo divisível por 3 e por 5."
    
    else:
        return "Número inválido"
    
numero_escolhido = int(input("Digite um número: "))
print (divisao(numero_escolhido))
