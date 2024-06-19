#Faça um programa que receba dois numeros e mostre o maior. 
#Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".

#Segunda Tarefa
def comparacao(numero1, numero2):
    if numero1 > numero2:   
        print(f"O número maior é: {numero1}")
    elif numero2 > numero1:
        print(f"O número maior é: {numero2}")
    else:
        print("Números iguais")
    
numero1 = int(input("Adicione um número: "))
numero2 = int(input("Adicione o segundo número: "))
comparacao(numero1,numero2)