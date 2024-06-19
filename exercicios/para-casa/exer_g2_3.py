# * Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou nao se aposentar. 
#   As condições para aposentadoria são:
#  • Ter pelo menos 65 anos,
#  • Ou ter trabalhado pelo menos 30 anos,
#  • Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos

def verificar_idade (idade, tempo_trab): 
    if idade >= 65:
        return "Apto para aposentadoria por idade"
    elif tempo_trab >= 30:
        return "Apto para aposentadoria por tempo de trabalho"
    elif idade >= 60 and tempo_trab == 25:
        return "Apto para aposentatoria por idade e tempo de trabalho"
    else:
        return "Não está apto para se aposentar."

idade = int(input("Qual a sua idade: "))
tempo_trab = int(input("Quanto tempo tem de trabalho: "))

retorno = verificar_idade (idade)
retorno2 = verificar_idade (tempo_trab)

print(f"idade")
print(f"tempo_trab")

