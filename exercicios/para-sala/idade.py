# 1. Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.

# idade = int(input("Qual a sua idade? : "))

# if idade >= 18:
#     print("Maior idade")
# else:
#     print("Menor idade")

# função

try:

    def validar_idade(idade):
    
        if idade >= 18:
            return "Maior idade"
        else:
            return "Menor idade"
    
    info_idade = int(input("Qual a sua idade? : "))

    print(validar_idade(info_idade))

except ValueError:
    print("Formato inválido, tente novamente")




