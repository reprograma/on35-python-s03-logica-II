## Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

def dia_semana(numero):
    if  numero > 0 and numero < 7:     
        return f"O dia da semana é {dias[numero]}." 
     
    else: numero > 7
    return "Número invalido."

dias= { 1 : "Domingo",
        2 : "segunda-feira",
        3 : "terça-feira",
        4 : "quata-feira:",
        5 : "quinta-feria",
        6 : "sexta-feira",
        7 : "sábado"
}
numero = int(input("adicione um número entre 1 e 7: "))

resposta = dia_semana(numero)
print(resposta)