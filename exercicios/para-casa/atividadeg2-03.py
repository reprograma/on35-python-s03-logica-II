#Exercício de Casa 🏠 Grupo 2
##Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou nao se aposentar. As condições para aposentadoria são:
###Ter pelo menos 65 anos, ou ter trabalhado pelo menos 30 anos, ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

idade_trabalhador = int(input("digite a sua idade: "))
tempo_de_servico = int(input("digite o tempo de trabalho: "))

if idade_trabalhador >= 65:
    print("Parabéns, voce tem idade e tempo de serviço adequada para aposentar")

elif tempo_de_servico >= 30:
     print("Parabéns, voce tem idade e tempo de serviço adequada para aposentar")

elif idade_trabalhador>= 60 and tempo_de_servico >= 25:
    print("Parabéns, voce tem idade e tempo de serviço adequada para aposentar")

else: 
    print("Infelizmente, você ainda naõ tem idade ou tempo de serviço para aposentar")


        

