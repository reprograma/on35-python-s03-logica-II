# 2. Faça um programa que mostre na tela uma pergunta de múltipla escolha, e que, a partir da resposta do usuário, mostre na tela se ele acertou ou não.

print("Qual é a capital da França?")

print("a) Londres")
print("b) Paris")
print("c) Roma")
print("d) Madrid")

resposta = input("Digite a resposta correta:").lower()

if resposta == "(b)":
    print("Parabéns você acertou!")

else:
    print("Você errou! A resposta correta é letra b, Paris.")

