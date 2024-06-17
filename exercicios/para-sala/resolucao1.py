# Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.

def verifica_idade(idade):
    if idade >= 18:
       return "Maior de idade"
    else:
       return "Não é maior de idade"

idade_inserida = int(input("Insira a idade da pessoa: "))
resultado = verifica_idade(idade_inserida)

print(resultado)

# try-except

try:
    def verifica_idade(idade):
        if idade >= 18:
            return "Maior de idade"
        else:
            return "Não é maior de idade"

    idade_inserida = int(input("Insira a idade da pessoa: "))
    resultado = verifica_idade(idade_inserida)

    print(resultado)

except ValueError:
    print("Dado inserido inválido")