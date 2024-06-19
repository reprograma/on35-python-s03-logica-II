# 3. Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.

nome = input("Qual o seu nome?")
resposta = input("Você gosta do seu nome? (sim ou não?)")

if resposta.lower() == "sim":
    print("Que bom que você gosta do seu nome!")
elif resposta.lower() == "não":
    print("Sinto muito que não gosta do seu nome!")
else:
    print("Resposta errada. Responda com 'sim' ou 'não'.")
