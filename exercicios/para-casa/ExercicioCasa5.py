def verificarAposentadoria(idade, tempoTrabalhado, genero):
    if genero.lower() == "homem":
        if idade >= 65 or tempoTrabalhado >= 30:
            return "Pode se aposentar."
        elif idade >= 60 and tempoTrabalhado >= 25:
            return "Pode se aposentar."
        else:
            return "Não pode se aposentar."
    elif genero.lower() == "mulher":
        if idade >= 65 or tempoTrabalhado >= 30:
            return "Pode se aposentar."
        elif idade >= 60 and tempoTrabalhado >= 25:
            return "Pode se aposentar."
        else:
            return "Não pode se aposentar."
    else:
        return "Gênero não reconhecido."


idade = int(input("Digite a idade: "))
tempoTrabalho = int(input("Digite os anos de trabalho: "))
genero = input("Digite o gênero: ")

resultado = verificarAposentadoria(idade, tempoTrabalho, genero)
print(resultado)
