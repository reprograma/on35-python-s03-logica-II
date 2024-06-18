# Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou nao se aposentar. As condições para aposentadoria são:
#  • Ter pelo menos 65 anos,
#  • Ou ter trabalhado pelo menos 30 anos,
#  • Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos

idade = int(input("Sua idade: "))
tempo_servico = int(input("Tempo de serviço: "))


def pode_aposentar(idade, tempo_servico):
    if idade >= 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25):
        return "Parabéns! Você pode se aposentar."
    else:
        return "Que pena! Você ainda não pode se aposentar."


resposta = pode_aposentar(idade, tempo_servico)

print(resposta)
