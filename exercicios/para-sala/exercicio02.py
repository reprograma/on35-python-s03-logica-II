#2. Faça um programa que mostre na tela uma pergunta de múltipla escolha, 
# e que, a partir da resposta do usuário, mostre na tela se ele acertou ou não.

melhor_carnaval = input("Onde é o melhor carnaval do Brasil? \n a - Rio de Janeiro \n b - São Paulo \n c - Olinda\n d - Salvador \n e - Belo Horizonte \nEscolha uma das alternativas: ")

if (melhor_carnaval == 'a') or (melhor_carnaval == 'b') or (melhor_carnaval == 'd') or (melhor_carnaval == 'e') :
    print('Sinto muito, você ainda não sabe qual o melhor carnaval do Brasil :( ')
elif (melhor_carnaval == "c") :
    print('Parabéns, você já sabe qual o melhor carnaval do Brasil :) ')
else:
    print("Resposta inválida")