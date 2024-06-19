# Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5, mas não simultaneamente pelos dois.

def verifica_divisivel(numero_inteiro):
    if (numero_inteiro % 3 == 0) and (numero_inteiro % 5 == 0):
        print('Numero escolhido é divisivel por 3 e por 5. Escolha outro numero')
    elif (numero_inteiro % 3 == 0):
        print(f'{numero_inteiro} é divisivel por 3')
    elif(numero_inteiro % 5 == 0):
        print(f'{numero_inteiro} é divisivel por 5')
    
    else:
        print('Numero escolhido não é divisivel por 3 ou 5')

numero_inserido = int(input(('Insira um numero: ')))
verifica_divisivel(numero_inserido)