## Faça um programa que mostre ao usuario um menu com 4 opções de operações matemáticas (as básicas, por exemplo). O usuário escolhe uma das opçõoes e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado.
def operacao_matematica(numero1,numero2,escolha):
    
    if escolha == 'adição':
        resultado = numero1 + numero2
        return f"O resultado da operação é: {resultado}."
    elif escolha == 'subtração':
        resultado = numero1 - numero2
        return f"O resultado da operação é: {resultado}."
    elif escolha == 'divisão':
        resultado = numero1 // numero2
        return f"O resultado da operação é: {resultado}."
    elif escolha == 'multiplicação':
        resultado = numero1 * numero2
        return f"O resultado da operação é: {resultado}."
    else:
        return "Operação inválida."

print("Opções de operações matematicas:",
      "\n adição",
      "\n divisão",
      "\n subtração",
      "\n multiplicação")      
escolha = input("Escolha uma das opções: ").lower()
numero1 = int(input("Ensira o primeiro número para realizar a operação: "))
numero2 = int(input("Ensira o segundo número para realizar a operação: "))

print(operacao_matematica(numero1,numero2,escolha))