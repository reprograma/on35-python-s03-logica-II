#Exercício: grupo 2

#* Faça um programa que mostre ao usuario um menu com 4 opções de operações matemáticas 
# (as básicas, por exemplo). O usuário escolhe uma das opçõoes e o seu programa 
# então pede dois valores numéricos e realiza a operação, mostrando o resultado.

def operacao (menu_escolha, numero1, numero2):
    if menu_escolha == "1" or menu_escolha == "adição":
        resultado= numero1 + numero2
    elif menu_escolha == "2" or menu_escolha == "subtração":
        resultado= numero1 - numero2
    elif menu_escolha == "3" or menu_escolha == "divisão":
        resultado= numero1 / numero2
    elif menu_escolha == "4" or menu_escolha == "multiplicação":
        resultado=numero1*numero2
    else:
        print("Operação inválida!")
        resultado = 0
    return resultado    

menu_escolha= input("Escolha uma opção, das operações da matemática abaixo: \n 1.adição \n 2.subtração \n 3.divisão \n 4.multiplicação\n: ")
numero1 = float(input("Coloque um número:"))
numero2= float(input("Coloque o segundo número:"))


resultado = operacao(menu_escolha, numero1, numero2)
print("Resultado: ", resultado)

#* Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5,
#  mas não simultaneamente pelos dois.


numero= int(input("Escolha um número inteiro:"))

if numero % 3 == 0:                                             # % resto da divisão
    print ("Este número é divisível por 3")

    
if numero % 5 == 0:
    print ("Este número é divisível por 5")


if numero % 5 != 0 or numero % 3 != 0:                            # != diferente, tudo que não for igual
    print("Este número não é divisível nem por 3 nem por 5!")
      


#* Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou nao se aposentar. 
# As condições para aposentadoria são:
#  • Ter pelo menos 65 anos,
# • Ou ter trabalhado pelo menos 30 anos,
#• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos

def aposentadoria (idade, tempo_trabalhado):
    if idade >= 65 or idade >= 60 and tempo_trabalhado>=25 or tempo_trabalhado>=30: 
        return "Você já pode se aposentar"
    else:
        return "Você ainda não pode se aposentar"

idade= int(input("Digite sua idade: "))
tempo_trabalhado= int(input("Digite seu tempo trabalhado em anos: "))

print (aposentadoria (idade,tempo_trabalhado))

