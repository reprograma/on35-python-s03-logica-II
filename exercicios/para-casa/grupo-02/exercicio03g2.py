#Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou nao se aposentar. As condições para aposentadoria são:
#  • Ter pelo menos 65 anos,
# • Ou ter trabalhado pelo menos 30 anos,
#  • Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos


def aposentadoria(idade,tempo_servico):
    if idade >= 65:
        print("Pode se aposentar!")
    elif tempo_servico >= 30:
        print("Pode se aposentar!")
    elif idade >= 60 and tempo_servico >= 25:
        print("Pode se aposentar!")
    else:
        print("Não pode se aposentar!")

idade = int(input("Idade: "))
tempo_servico = int(input("Tempo de serviço: "))

aposentadoria(idade,tempo_servico)

