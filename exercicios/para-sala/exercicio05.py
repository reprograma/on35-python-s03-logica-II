#5. Faça um programa que permita o usuário escolher entre três opções de bebidas e mostre na tela a bebida escolhida.

bebida = input("Escolha uma bebida: \n a - cerveja \n b - agua \n c - refrigerante \nEscolha uma das alternativas: ")

if bebida == 'a' or bebida == 'cerveja':
    print('Você escolheu cerveja')
elif bebida == "b" or bebida == 'agua':
    print('Você escolheu água')
elif bebida == 'c' or bebida == "refrigerante":
    print('Você escolheu refrigerante')
else:
    print("Resposta inválida")