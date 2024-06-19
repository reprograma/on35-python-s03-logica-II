
# * Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. 
# Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

def numero_semana(numero):
    if numero == 1:
        return f"O número {numero} corresponde a Domingo!"
    if numero == 2:
        return f"O número {numero} corresponde a Segunda-feira!"
    if numero == 3:
        return f"O número {numero} corresponde a Terça-feira!"
    if numero == 4:
        return f"O número {numero} corresponde a Quarta-feira!"
    if numero == 5:
        return f"O número {numero} corresponde a Quinta-feira!"
    if numero == 6:
        return f"O número {numero} corresponde a Sexta-feira"
    if numero == 7:
        return f"O número {numero} corresponde a Sábado!"



numero = int(input("Digite um número de 1 a 7: "))
resposta = numero_semana(numero)
print(resposta)