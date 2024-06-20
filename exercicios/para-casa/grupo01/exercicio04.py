#Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.
input("tem limite de idade para este jogo?")
def verifica_idade(resposta):

    if resposta <= 18:

        return 'Que legal, você pode participar!'

    elif resposta > 18:

        return 'Entendi, você já está com idade para outro jogo, pois já é maior de idadecd'

    else:

        return 'acesso negado'

idadeInserida1 = int(input('insira a idade da pessoa 1: '))
resultado1 = verifica_idade(idadeInserida1)

idadeInserida2 = int(input("insira a idade da pessoa 2: "))
resultado2 = verifica_idade(idadeInserida2)

print(f"pessoa 1: {resultado1}")   
print(f"pessoa 2: {resultado2}") 

try:
    idade = int(input("Insira sua idade: "))
    if idade <= 18:
        print("Você pode jogar!")
    else:
        print("Desculpe, você não tem idade suficiente para jogar.")
except ValueError:
    print("Idade inválida. Digite um número inteiro.")
except Exception as e:
    # Se um erro inesperado ocorrer
    print(f"Ocorreu um erro: {e}")
