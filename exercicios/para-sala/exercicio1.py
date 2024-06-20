#Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.

def verificar_maioridade(idade):

    if idade >=18:
        return 'Você é maior de idade'
    else:
        return "você não é maior de idade"
    
idade = int(input("Digite sua idade: "))
resultado = verificar_maioridade(idade)

print(resultado)


    


    

    





