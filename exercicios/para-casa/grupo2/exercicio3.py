##Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou nao se aposentar. As condições para aposentadoria são:
 ## • Ter pelo menos 65 anos,
 ## • Ou ter trabalhado pelo menos 30 anos,
 ## • Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos

def aposentadoria(idade,tempo_de_serviço):
    if idade >= 65:
        return " atende os resquisitos para aposentadoria por idade"
    elif tempo_de_serviço >= 30:
        return "atende os resquisitos por tempo de contribuição"
    elif idade >= 60 and tempo_de_serviço >= 25:
        return "atende ambos requisitos para aponsentadoria "
    else:
        return "Não atende nenhum dos resquisitos para aposentadoria"


idade = int(input("Preencha a sua idade: "))
Tempo_de_serviço = int(input("Preencha seu tempo de contribuição: "))

print(aposentadoria(idade,Tempo_de_serviço))