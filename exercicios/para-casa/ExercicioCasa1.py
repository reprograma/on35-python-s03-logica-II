def mostrarNumero():
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        
        if num1 > num2:
            print(f"O maior número é {num1}")
        elif num2 > num1:
            print(f"O maior número é {num2}")
        else:
            print(f"Os números são iguais: {num1} e {num2}")

        diferenca = abs(num1 - num2)  #abs é uma função que faz o número voltar positivo
        print(f"A diferença entre eles é {diferenca}")
    except ValueError:
        print("Por favor, digite números inteiros válidos.")

mostrarNumero()

