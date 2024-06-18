# 2. Faça um programa que mostre na tela uma pergunta de múltipla escolha, e que, a partir da resposta do usuário, mostre na tela se ele acertou ou não.

print("Qual o maior órgão do corpo humano?",
      "\n a. Cérebro",
      "\n b. Pele",
      "\n c. Coração",
      "\n d. Pulmão")

resposta = input("Insira a letra correspondente a sua resposta: ")

if resposta.lower() == "b":
    print("Resposta certa!")
else:
    print("Resposta incorreta.")
