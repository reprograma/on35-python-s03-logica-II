def aposentadoria():

    idade=int(input("\nInforme sua idade: "))
    tempo_servico=int(input("Informe o tempo de serviço: "))
    if idade>= 65 or tempo_servico == 30:
        print("Pode se aposentar :)")
    elif idade == 60 and tempo_servico == 25:
        print("Pode se aposentar :)")
    else:
        print("Não pode se aposentar :(")

aposentadoria()