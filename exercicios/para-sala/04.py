#Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, pergunte quantos e mostre na tela uma mensagem de sua escolha. No caso de o usuário responder “não”, pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.
resposta = input('Você possui irmãos? (sim/não): ')

if resposta.lower() == "sim":
quantidade = int(input("Quantos irmãos você tem? ")) 
print(f'Você tem {quantidade} irmão(s)')

elif resposta.lower() == 'não': 
gostaria = input('Você gostaria de ter irmãos? (sim/não): ')
if gostaria.lower() == 'sim': 
 print('Legal!')
 elif: gostaria.lower() == 'não': 
print('Entendo, nem todo  mundo quer.')