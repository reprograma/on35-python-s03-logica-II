#Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5, mas não simultaneamente pelos dois.
def divisao (numero):
    if numero % 3 == 0 and numero % 5 == 0: 
        return False 
    elif numero % 3 == 0 or numero % 5 == 0: 
        return True
    else: 
        return False 
    
numero = int(input("Digite um número inteiro: "))

if divisao (numero):
    print(f"O número {numero} é divisível por 3 ou por 5, mas não simultaneamente.")
else: 
    print(f"O número {numero} não atende aos critérios especificados.")
    
    