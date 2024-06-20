#Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou nao se aposentar. As condições para aposentadoria são:
  #• Ter pelo menos 65 anos,
  #• Ou ter trabalhado pelo menos 30 anos,
  #• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos

def aposentadoria(idade,trabalho,):
 
  if (idade >= 65 or trabalho >= 30) or (idade>=60 and trabalho >= 25):
    return "Você está apto para aposentadoria!"
  else:
    return "Você ainda não está apto para se aposentar"

idade= int(input("Qual é a sua idade? "))
trabalho= int(input("Quantos anos você trabalhou? "))

print(aposentadoria(idade,trabalho))

