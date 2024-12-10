#Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou nao se aposentar. As condições para aposentadoria são: 
# • Ter pelo menos 65 anos, • Ou ter trabalhado pelo menos 30 anos, • Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos

idade = int (input("Insira sua idade (em anos): "))
tempo_trabalhado = int (input("Insira seu tempo trabalhado (em anos): "))

if idade >= int (65):
    print ("Apto para aposentadoria")
elif tempo_trabalhado >= int (30):
    print ("Apto para aposentadoria")
elif idade >= int (30) and tempo_trabalhado >= int (25):
    print ("Apto para aposentadoria")
else:
    print ("Não apto para aposentadoria")
    
