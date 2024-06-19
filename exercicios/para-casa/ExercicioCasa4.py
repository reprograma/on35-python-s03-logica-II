def divisivel(num):
    if num % 3 == 0 and num == 0:
        return f"{num} é divisível por 3 e por 5."
    elif num % 3 == 0:
        return f"{num} é divisível por 3, mas por 5 não."
    elif num % 5 == 0:
        return f"{num} é divisível por 5, mas por 3 não."
    else:
        return f"{num} não é divisível nem por 3 e nem por 5."
    

numDigito = int(input("Digite um número inteiro: "))
print(divisivel(numDigito))