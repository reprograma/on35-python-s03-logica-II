def mostrarDia(num):
    if num == 1:
        print("Domingo")
    elif num == 2:
        print("Segunda-feira")
    elif num == 3:
        print("Terça-feira")
    elif num == 4:
        print("Quarta-feira")
    elif num == 5:
        print("Quinta-feira")
    elif num == 6:
        print("Sexta-feira")
    elif num == 7:
        print("Sábado")
    else:
        print("Número inválido. Digite um valor entre 1 e 7.")

numeroDigitado = int(input("Digite um número entre 1 e 7: "))
mostrarDia(numeroDigitado)
