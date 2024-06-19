# Exercício: grupo 1


##* Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.


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


##* Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".

n1 = int(input("Fala outro número -> "))
n2 = int(input("Fala mais outro -> "))

def maior_n (n1, n2):
    if n1>n2:
        return(f"O {n1} é o maior entre os que você nos forneceu")
    elif n1<n2:
        return(f"O {n2} é o maior entre os que você nos forneceu")
    elif n1 == n2:
        return("Números iguais")

total = maior_n(n1, n2)
print(total)


##* Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

num = int(input("Me diz um outro número, mas agora entre 1 e 7 -> "))

def numero_da_semana(num):
    if num == 1:
        return("Esse número corresponde ao dia da semana domingo")
    elif num == 2:
        return("Esse número corresponde ao dia da semana segunda-feira")
    elif num == 3:
        return("Esse número corresponde ao dia da semana terça-feira")
    elif num == 4:
        return("Esse número corresponde ao dia da semana quarta-feira")
    elif num == 5:
        return("Esse número corresponde ao dia da semana quinta-feira")
    elif num == 6:
        return("Esse número corresponde ao dia da semana sexta-feira")
    elif num == 7:
        return("Esse número corresponde ao dia da semana sábado")
    else:
        return("Esse número nao vale, tem que ser entre 1 e 7 :/")
    
resultado_dia_da_semana = numero_da_semana(num)
print(resultado_dia_da_semana)

