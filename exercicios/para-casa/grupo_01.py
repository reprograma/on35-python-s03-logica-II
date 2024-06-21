#Exercício: grupo 1

#* Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, 
# assim como a diferença existente entre ambos.

def numeros(x, y):
    if x>y:
        diferenca= x - y
        return (f"O número maior é o {x} e a diferença entre eles é {diferenca}")
    elif y> x:
        diferenca=y-x
        return (f"O número maior é o {y} e a diferença entre eles é {diferenca}")
  
numero1=int(input ("Digite um número: "))
numero2=int(input ("Digite outro número: "))

resultado=numeros(numero1,numero2)
print (resultado)

#* Faça um programa que receba dois numeros e mostre o maior. 
# Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".


def numeros(x, y):
    if x>y:
        diferenca= x - y
        return (f"O número maior é o {x} e a diferença entre eles é {diferenca}")
    elif y> x:
        diferenca=y-x
        return (f"O número maior é o {y} e a diferença entre eles é {diferenca}")
    else:
        return ("Números iguais")
  
numero1=int(input ("Digite um número: "))
numero2=int(input ("Digite outro número: "))

resultado=numeros(numero1,numero2)
print (resultado)


#* Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana 
# correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

dias_semana = ["","domingo", "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado"]

dia_semana=int(input("Digite um número entre 1 a 7: "))               

print(f"O dia da semana referente a esse número é {dias_semana[dia_semana]}")         #dúvida nesse formato

