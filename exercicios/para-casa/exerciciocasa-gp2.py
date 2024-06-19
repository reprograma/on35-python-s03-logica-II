#Faça um programa que mostre ao usuario um menu com 4 opções de operações matemáticas (as básicas, por exemplo). 
#O usuário escolhe uma das opçõoes e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado.
#* Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5, mas não simultaneamente pelos dois.
#* Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou nao se aposentar. As condições para aposentadoria são:
#  • Ter pelo menos 65 anos,
#  • Ou ter trabalhado pelo menos 30 anos,
#  • Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos

#Primeira Tarefa
def menu():
    print("\n Escolha uma Operação Matemática:  \n 1. Adição \n 2. Subtração \n 3. Multiplicação \n 4. Divisão")

def matematica(numero1, numero2, opcao):
    if opcao == 1:
        return numero1 + numero2
    elif opcao == 2:
        return numero1 - numero2
    elif opcao == 3:
        return numero1 * numero2
    elif opcao == 4:
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "ERRO"
    else:
        return "Inválido"

menu()
opcao = int(input("Digite a opção da operação matemática: "))
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

resultado = matematica(numero1, numero2, opcao)
print(f"O resultado é: {resultado}")