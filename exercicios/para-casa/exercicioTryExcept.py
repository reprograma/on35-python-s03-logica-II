# 1. Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.

try:
    idade_informada = int(input("Informe sua idade: "))
except ValueError:
    print("Informe um valor válido para a idade.")
else:
    def verifica_idade(idade):
        if idade >= 18:
            return "Usuário é maior de idade"
        else:
            return "Usuário não é maior de idade"

    resultado = verifica_idade(idade_informada)

    print(resultado)
