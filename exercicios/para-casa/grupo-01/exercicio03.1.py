dias_semana = {
    1: "Domingo",
    2: "Segunda",
    3: "Terça",
    4: "Quarta",
    5: "Quinta",
    6: "Sexta",
    7: "Sábado"
}

dia_semana = int(input("Digite um número de 1 a 7: "))

if dia_semana in dias_semana:
    print(dias_semana[dia_semana])
else:
    print("Resposta inválida.")