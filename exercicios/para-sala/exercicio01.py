#Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.
def verifica_idade(idade):
    if idade>=18:
        return "\n você é maior de idade,\n"
    else: return "\n você é menor de idade\n"

idade_inserida = int(input("\n Digite sua idade:"))

Resposta = print(verifica_idade(idade_inserida))
