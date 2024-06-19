# 2. Faça um programa que mostre na tela uma pergunta de múltipla escolha, e que, a partir da resposta do usuário, 
# mostre na tela se ele acertou ou não.

def perguntar():
    print("Qual é a capital do Brasil?")
    print("a) Natal")
    print("b) Salvador")
    print("c) Curitiba")
    print("d) Belo Horizonte")

    resposta_correta = "c"
    resposta_usuario = input("Digite a opção correta: ")

    if resposta_usuario() == resposta_correta:
        print("Parabéns! Você acertou!")
    else:
        print("Você errou. A resposta correta é 'c) Curitiba")


