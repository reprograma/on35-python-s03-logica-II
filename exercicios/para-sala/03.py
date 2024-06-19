#Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.
nome = input('Digite um nome:  ')
gosta_nome = input(f"Você gosta do nome'{nome}'?(sim/não): ")

if nome == 'sim': 
   print(f"Que bom que você gosta do nome '{nome}'")
else: 
   print(f"Poxa, que pena que você não gosta do nome '{nome}'")