# Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.

def verifica_idade(idade):
    if idade <=17:
        return "Usuario menor de idade"
    else:
        return "Usuario maior de idade"
    
idade_inserida = int(input("Digite a sua idade: "))
resultado = verifica_idade(idade_inserida)

print(f"Mensagem: {resultado}")


