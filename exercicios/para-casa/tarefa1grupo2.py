# Faça um programa que mostre ao usuario um menu com 4 opções de operações matemáticas (as básicas, por exemplo).
# O usuário escolhe uma das opçõoes e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado.

operacao_escolhida = input("Escolha uma das operações matemáticas:\n"
                           "a. Adição (+)\n"
                           "b. Subtração (-)\n"
                           "c. Multiplicação (*)\n"
                           "d. Divisão (/)\n"
                           "Digite a letra correspondente a operação escolhida: ").lower()

valor1 = float(input("Digite o primeiro número: "))
valor2 = float(input("Digite o segundo número: "))


def calcula(valor1, valor2):
    if operacao_escolhida == "a":
        return valor1 + valor2
    elif operacao_escolhida == "b":
        return valor1 - valor2
    elif operacao_escolhida == "c":
        return valor1 * valor2
    elif operacao_escolhida == "d":
        return valor1 / valor2
    else:
        return "Opção inválida!"


resultado = calcula(valor1, valor2)

print(f"O resultado é {resultado}")
