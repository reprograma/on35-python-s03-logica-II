# Exercício: grupo 1
##* Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.
##* Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".
##* Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.




numero1 = int(input("Insira um número inteiro ->"))
numero2 = int(input("Insira um outro número inteiro ->"))

diferença_entre_eles = numero1 - numero2 

def qual_maior_numero(numero1, numero2):
    
    if numero1 > numero2:
        return(f"O {numero1} é o maior entre os que você nos forneceu, e a diferença entre eles é de {diferença_entre_eles}")
    elif numero1 < numero2:
        return(f"O {numero2} é o maior entre os dois que você nos forneceu, e a diferença entre eles é de {diferença_entre_eles}")
    
resultado = qual_maior_numero(numero1, numero2)
print(resultado)