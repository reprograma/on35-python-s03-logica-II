#Faça um programa que permita o usuário escolher entre três opções de bebidas e mostre na tela a bebida escolhida.
print("Escolha a sua bebida favorita:")
print('1) Café')
print('2) Suco')
print('3) Cerveja')

escolha = input('Digite o número que você escolheu (1, 2 ou 3): ')
if escolha == '1': 
    print('Você escolheu Café')
elif escolha == '2': 
    print('Você escolheu Suco')
elif escolha == '3':
    print('Você escolheu Cerveja')