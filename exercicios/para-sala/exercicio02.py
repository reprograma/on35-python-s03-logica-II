#Faça um programa que mostre na tela uma pergunta de múltipla escolha, e que, a partir da resposta do usuário, mostre na 
#tela se ele acertou ou não.

def  esportes_olimpicos(escolha):
    if escolha ==  "c":
        return "\n Este será um esporte dos jogos olimpicos 2024\n"
    elif escolha == "a" or "b" or "d":
        return "\n Em 2024 este não será um esporte olimpico!\n"


escolha = input("Qual o unico esporte que fará parte dos jogos olimpicos 2024:\n A - Beisebol \n B - karate \n C - Breaking Dance \n D - Softbol \n")
Resposta_escolhida = print (esportes_olimpicos(escolha)) 


