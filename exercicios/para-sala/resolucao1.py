# Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.

def verifica_idade(idade):
    if idade >= 18:
       return "Maior de idade"
    else:
       return "Não é maior de idade"

idade_inserida = int(input("Insira a idade da pessoa: "))
resultado = verifica_idade(idade_inserida)

print(resultado)

# Caso fosse inserido um dado do tipo string no programa, o código não irá rodar 
# por conta de erro do tipo de execução.
