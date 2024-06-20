#   • Ter pelo menos 65 anos,
#   • Ou ter trabalhado pelo menos 30 anos,
#   • Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos

def aposentadoria():
    idade = int(input(" Informe sua idade ? : "))
    tempo_servico= int(input(" Informe seu tempo de serviço ? : "))

    if idade >= 65:
        print("Você já pode se aposentar por idade")

    elif tempo_servico >=30:
        print("Você já pode se aposentar por tempo de serviço")
    
    elif idade >= 60 and tempo_servico >= 25 :
        print ("Você possui idade e tempo de serviço para se aposentar")

    else:
        print("Você não possui os critérios necessários para aposentadoria")

aposentadoria()
