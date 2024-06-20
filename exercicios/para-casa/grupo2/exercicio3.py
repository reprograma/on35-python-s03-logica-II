##Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou nao se aposentar. As condições para aposentadoria são:
 ## • Ter pelo menos 65 anos,
 ## • Ou ter trabalhado pelo menos 30 anos,
 ## • Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos

def aposentadoria(idade,tempo_de_serviço):
    if idade >= 65:
        return " Atende os resquisitos para aposentadoria por idade"
    elif tempo_de_serviço >= 30:
        return "Atende os resquisitos por tempo de contribuição"
    elif idade >= 60 and tempo_de_serviço >= 25:
        return "Atende ambos requisitos para aponsentadoria "
    else:
        return "Não atende nenhum dos resquisitos para aposentadoria"


idade_contribuinte = int(input("Preencha a sua idade: "))
tempo_de_contribuição = int(input("Preencha seu tempo de contribuição: "))

print(aposentadoria(idade_contribuinte,tempo_de_contribuição))