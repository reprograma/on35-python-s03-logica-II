#Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

def dia_da_semana(inteiro):
    if inteiro == 1:
        return "Domingo"
    
    elif inteiro == 2:
        return "Segunda-feira"
    
    elif inteiro == 3:
        return "Terça-feira"
    
    elif inteiro == 4:
        return "Quarta-feira"
    
    elif inteiro == 5:
        return "Quinta-feira"
    
    elif inteiro == 6:
        return "Sexta-feira"
    
    elif inteiro == 7:
        return "Sábado"
    else:
        return "O número digitado não corresponde ao solicitado"


inteiro = int(input("Digite um número entre 1 e 7:"))

resultado = dia_da_semana(inteiro)

print(resultado)