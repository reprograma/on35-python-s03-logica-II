#Faça um programa que permita o usuário escolher entre três opções de bebidas e mostre na tela a bebida escolhida.

bebida = input("Escolha uma bebida: \n a - água \n b - cerveja \n c - refrigerante \n Escolha uma das alternativas: ")

if bebida == 'a' or bebida == 'água':
    print('Você escolheu água')
elif bebida == 'b' or bebida == 'cerveja':
    print ('Você escolheu certeja')
elif bebida == 'c' or bebida == "refrigerante":
    print ('Você escolheu refrigerente')
else:
    print("Resposta inválida")