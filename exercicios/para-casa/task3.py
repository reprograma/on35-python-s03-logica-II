#* Faça um programa que receba dois numeros e mostre o maior. 
# Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".

def biggestnumb(numb1, numb2):
    if numb1 > numb2:
        biggest = numb1
    else:
        biggest = numb2
    return biggest


def equalnumb(numb1, numb2):
    if numb1 == numb2:
         return "Números iguais"

#ask for input
input1 = float(input("Insira um número: "))
input2 = float(input("Insira um número: "))
biggest = biggestnumb(input1, input2)
equal = equalnumb(input1, input2)

print (f"O maior número é: {biggest}")
print (f"{equal}")