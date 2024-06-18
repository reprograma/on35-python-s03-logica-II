# * Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5, mas não simultaneamente pelos dois.

#3 ou 5
#não 3 e 5 

def verificadordivisão (numero):
       
    if (numero % 3 == 0 and numero % 5 != 0) or (numero % 3 != 0 and numero % 5 == 0):
        return 'Esse número é válido'
    
    else: 
        return 'Esse número é inválido'

numero = int(input("Por favor, insira um número:  "))
print(verificadordivisão(numero))
        
