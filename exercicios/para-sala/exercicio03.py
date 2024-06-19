#3. Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, 
# em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.

nome = input("Insira seu nome: ")

gosta_nome = input("Você gosta do seu nome? s/n ")

if (gosta_nome == "S"):
    print('Que bom! É um nome lindo mesmo!')
else:
    print("Sério? Que pena, é um nome tão bonito!")