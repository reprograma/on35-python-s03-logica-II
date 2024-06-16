# Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e,
# em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.


nome = input("Como você se chama?")
gosta_nome = input (f"Você gosta do seu nome{nome}? \n (Sim/Não): ")

if gosta_nome == "Sim":
  print("Também gosto do seu nome!")
else:
   print("Poxa, mas eu gosto do seu nome.")