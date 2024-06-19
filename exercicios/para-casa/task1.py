#Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.

def biggestnumb(numb1, numb2):
    if numb1 > numb2:
        biggest = numb1
    else:
        biggest = numb2
    return biggest


def diff(numb1, numb2):
    if numb1 > numb2:
        diff = numb1 - numb2
    else:
        diff = numb2 - numb1

    return diff

#ask for input
input1 = int(input("Insira um número inteiro: "))
input2 = int(input("Insira um número inteiro: "))
biggest = biggestnumb(input1, input2)
difference = diff(input1, input2)

print (f"O maior número é: {biggest}")
print (f"A diferença entre os números inseridos é: {difference}")