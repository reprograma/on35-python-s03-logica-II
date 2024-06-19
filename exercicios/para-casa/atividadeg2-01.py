#Exercício de Casa 🏠 Grupo 2

##Faça um programa que mostre ao usuario um menu com 4 opções de operações matemáticas (as básicas, por exemplo).
### O usuário escolhe uma das opçõoes e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado.

def adicao(num1, num2):
  return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Erro: Divisão por zero!"

operacoes = {
    '1': adicao,
    '2': subtracao,
    '3': multiplicacao,
    '4': divisao
}

def mostrar_menu():
    print("Escolha uma operação matemática:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")

def main():
    mostrar_menu()
    opcao = input("Digite o número da operação desejada: ")

    if opcao not in operacoes:
        print("Opção inválida! Programa encerrado.")
        return

    try:
        num1 = float(input("Digite o primeiro valor: "))
        num2 = float(input("Digite o segundo valor: "))
    except ValueError:
        print("Por favor, digite valores numéricos válidos. Programa encerrado.")
        return

    # Chama a função correspondente à operação escolhida
    resultado = operacoes[opcao](num1, num2)
    print(f"O resultado da operação é: {resultado}")

if __name__ == "__main__":
    main()