# * Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5, mas não simultaneamente pelos dois.

#3 ou 5
#não 3 e 5 

def verificadordivisão (numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'Esse número é divisivel por três e cinco'
        
    elif numero % 3 == 0 or numero % 5 != 0:
        return 'Esse número é divisivel apenas pelo número três'
    
    elif numero % 3 != 0 or numero % 5 == 0:
        return 'Esse número é divisivel apenas pelo número cinco'
    
    else: 
        return 'Esse número não é divisível por três, nem por cinco'

numero = int(input("Por favor, insira um número:  "))
print(verificadordivisão(numero))
        
