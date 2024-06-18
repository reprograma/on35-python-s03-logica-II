# * Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou nao se aposentar. As condições para aposentadoria são:
#   • Ter pelo menos 65 anos,
#   • Ou ter trabalhado pelo menos 30 anos,
#   • Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos

def pode_aposentar (idade, temposervico):
    if idade >= 65 or temposervico >= 30 or (idade >= 60 and temposervico >= 25):
        return 'Que bom! Você já pode se aposentar!'
    else:
        return 'Que pena! Você ainda não pode se aposentar!'
    
idade = int(input ('Por favor, insira a sua idade: '))
temposervico = int(input ('Por favor, insira o seu tempo de serviço: '))
print(pode_aposentar(idade, temposervico))