# Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou nao se aposentar. 
# As condições para aposentadoria são: • Ter pelo menos 65 anos, • Ou ter trabalhado pelo menos 30 anos, 
# • Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos

def consegue_se_aposentar(idade, tempo_servico):
    # Verifica as condições para aposentadoria
    if idade >= 65:
        return True
    elif tempo_servico >= 30:
        return True
    elif idade >= 60 and tempo_servico >= 25:
        return True
    else:
        return False

idade = int(input("Digite a idade do trabalhador: "))
tempo_servico = int(input("Digite o tempo de serviço do trabalhador (em anos): "))

if consegue_se_aposentar(idade, tempo_servico):
    print("O trabalhador tem tempo de aposentadoria.")
else:
    print("O trabalhador não tem tempo de aposentadoria.")