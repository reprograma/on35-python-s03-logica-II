dias_semana = ["", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado", "Domingo"]

dia_escolhido = int(input("Considerando que \n 1 Domingo \n 2 Segunda-feira \n 3 Terça-feira \n 4 Quarta-feira \n 5 Quinta-feira \n 6 Sexta-feira \n 7 Sabado \n Insira o código do dia da semana que deseja visualizar:  "))

print(f"Dia da semana correspondente ao numero {dia_escolhido} é {dias_semana[dia_escolhido]}")