try:
    idade = int(input("Digite sua idade: "))
    if idade < 0:
        print("Idade não pode ser negativa.")
    elif idade >= 18:
        print("Você é maior de idade!")
    else:
        print("Você é menor de idade!")
except ValueError:
    print("Por favor, digite um número inteiro válido.")