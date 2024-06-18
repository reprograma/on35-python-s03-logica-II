def divisivel():
    numero=int(input("\nInforme um número inteiro: "))

    if numero % 3 == 0 and numero % 5 == 0:
        print("\nÉ divisível por 3 e 5.")
    elif numero % 3 == 0:
        print(f"É divisível por 3")
    elif numero % 5 == 0:
        print("É divisível por 5")
    else:
        print("Não é divisivel por 3 ou 5 :(\nTente novamente!")

divisivel()