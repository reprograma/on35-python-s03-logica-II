# 2. Faça um programa que mostre na tela uma pergunta de múltipla escolha, e que, a partir da resposta do usuário, mostre na tela se ele acertou ou não.

def capital_argentina(resposta):
    if resposta == "B":
        return "Certa resposta!"
    elif resposta == "A" or "C" or "D":
        return "Resposta errada!"

pergunta = input("Qual é a capital da Argentina? A/ São Paulo B/ Buenos Aires C/ Santiago D/ Madrid ")
dada_resposta = print(capital_argentina(pergunta))
