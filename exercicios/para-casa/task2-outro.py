#Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. 
#Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

#>list< é uma lista dentro do python pra fazer resultados sequenciais etc
weekdays = ["dom","seg","ter","qua","qui","sex","sab"]

#o python sempre começa contando do zero, por isso subtrai 1 do input de dia
def weekday_clean(day):
    if day > 7 or day < 1:
        return "dia invalido"
    return weekdays[day-1]

def weekday(numb):
    if numb == 1:
        return "domingo"    
    elif numb == 2:
        return "segunda"
    elif numb == 3:
        return "terça"
    elif numb == 4:
        return "quarta"
    elif numb == 5:
        return "quinta"
    elif numb == 6:
        return "sexta"
    elif numb == 7:
        return "sábado"
    else:
        return "número inválido"
        
#ask for input
numb1 = int(input("Insira um número inteiro entre 1 e 7: "))
result = weekday(numb1)
result_clean = weekday_clean(numb1)

print(f"resultado da funcao com if: {result}")
print(f"resultado da funcao limpa(com lista): {result_clean}")
