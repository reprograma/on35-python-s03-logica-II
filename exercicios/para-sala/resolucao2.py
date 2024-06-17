# Faça um programa que mostre na tela uma pergunta de múltipla escolha, e que, a partir da resposta
# do usuário, mostre na tela se ele acertou ou não.


pergunta = input (f"Qual álbum da Lorde foi lançado em 2017?")
opcao_a = input ("a) Pure Heroine")
opcao_b = input ("b) Melodrama")
opcao_c = input ("c) Solar Power")

resposta_usuario = input("Digite sua resposta: ")

if resposta_usuario == "b) Melodrama" or resposta_usuario == "b" or resposta_usuario == "Melodrama":
    print("Você acertou!")
else:
    print("Resposta incorreta.")