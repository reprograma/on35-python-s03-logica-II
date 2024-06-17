# Faça um programa que permita o usuário escolher entre três opções de bebidas e mostre na tela 
# a bebida escolhida.


pergunta = input (f"Escolha uma bebida: ")
opcao_a = input ("a) Mate")
opcao_b = input ("b) Refrigerante")
opcao_c = input ("c) Água")

resposta_usuario = input("Digite sua escolha: ")

if resposta_usuario == "a) Mate" or resposta_usuario == "a" or resposta_usuario == "Mate":
 print ("Você escolheu mate.")
elif resposta_usuario == "b) Refrigerante" or resposta_usuario == "b" or resposta_usuario == "Refrigerante":
  print ("Você escolheu refrigerante.")
elif resposta_usuario == "c) Água" or resposta_usuario == "c" or resposta_usuario == "Água":
  print ("Você escolheu água.")
else:
    print("Escolha inválida. Escolha uma das três bebidas.")