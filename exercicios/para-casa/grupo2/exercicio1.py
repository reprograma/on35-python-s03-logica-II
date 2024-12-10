## Faça um programa que mostre ao usuario um menu com 4 opções de operações matemáticas (as básicas, por exemplo). O usuário escolhe uma das opçõoes e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado.
def operacao_matematica(numero1,numero2,escolha):
    
    if escolha == 'adição':
        resultado = numero1 + numero2
        return f"O resultado da operação é: {resultado}"
    elif escolha == 'subtração':
        resultado = numero1 - numero2
        return f"O resultado da operação é: {resultado}"
    elif escolha == 'divisão':
        resultado = numero1 / numero2
        return f"O resultado da operação é: {resultado}"
    elif escolha == 'multiplicação':
        resultado = numero1 * numero2
        return f"O resultado da operação é: {resultado}"
    else:
        return "Operação inválida."

print("Opções de operações matematicas:",
      "\n adição",
      "\n divisão",
      "\n subtração",
      "\n multiplicação")      
operacao = input("Escolha uma das opções: ").lower()
primeiro_numero = int(input("Insira o primeiro número para realizar a operação: "))
segundo_numero = int(input("Insira o segundo número para realizar a operação: "))

print(operacao_matematica(primeiro_numero,segundo_numero,operacao))