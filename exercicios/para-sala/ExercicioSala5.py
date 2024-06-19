def mostrarCardapio():
    print("Escolha uma comida:")
    print("1. Salada")
    print("2. Pizza")
    print("3. Sopa")

mostrarCardapio()
escolha = int(input("Digite o número da comida desejada (1, 2 ou 3): "))

if escolha == 1:
        print("Você escolheu Salada.")
elif escolha == 2:
        print("Você escolheu Pizza.")
elif escolha == 3:
        print("Você escolheu Sopa.")
else:
        print("Opção inválida. Escolha entre 1, 2 ou 3.")
