# 5. Faça um programa que permita o usuário escolher entre três opções de bebidas e mostre na tela a bebida escolhida.

resposta = input("Escolha uma bebida:\n"
                 " 1. Café\n"
                 " 2. Café com leite\n"
                 " 3. Cappuccino\n"
                 "Insira o número da bebida escolhida: ")

if resposta == "1":
    print("Você escolheu café!")
elif resposta == "2":
    print("Você escolheu café com leite!")
elif resposta == "3":
    print("Você escolheu cappuccino!")
else:
    print("Opção inválida")
