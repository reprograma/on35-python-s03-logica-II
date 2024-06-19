#Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou nao se aposentar. As condições para aposentadoria são:
  #• Ter pelo menos 65 anos,
  # Ou ter trabalhado pelo menos 30 anos,
  #• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos
 
def requisitos_aposentadoria(idade, tempo_servico):

    if idade >= 65:
        return ("Preenche requisitos") 
    elif tempo_servico >=30:
        return ("Preenche requisitos") 
    elif idade >= 60 and tempo_servico >=25:
        return ("Preenche requisitos") 
    else: 
        return ("Não preenche requisitos") 

idade = int(input("Qual a sua idade? "))
tempo_servico = float(input("Quanto tempo de servico? "))
print(requisitos_aposentadoria(idade, tempo_servico))