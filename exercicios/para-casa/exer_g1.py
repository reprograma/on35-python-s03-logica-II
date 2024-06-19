# Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, \n 
# assim como a diferença existente entre ambos.

# Faça um programa que receba dois numeros e mostre o maior. Se por acaso, \n
# os dois números forem iguais, imprima a mensagem "Números iguais".

def verificar_numero (num1,num2):
    if num1 > num2:
        diferenca = num1 - num2
        return "O maior número é {num1} e a diferença entre eles é de {diferenca}"

    elif num2 > num1:
        diferenca = num2 - num1
        return "O maior número é {num2} e a diferença entre eles é de {diferenca}"

    else:
        return "Números iguais."

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resultado = verificar_numero(num1,num2)
print(resultado)
# Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente \n
# a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

dia_semana = int(input("Digite o número de 1 a 7 para representar os dias da semana (iniciando no domingo):"))
# Estou confusa como fazer o 'def' nessa questão
if dia_semana == 1:
    print("O dia da semana é domingo")
elif dia_semana == 2:
    print("O dia da semana é Segunda")
elif dia_semana == 3:
    print("O dia da semana é Terça")
elif dia_semana == 4:
    print("O dia da semana é Quarta")
elif dia_semana == 5:
    print("O dia da semana é Quinta")  
elif dia_semana == 6:
    print("O dia da semana é Sexta") 
elif dia_semana == 7:
    print("O dia da semana é Sabado")       
else:
    print("Favor, digite um número válido")
