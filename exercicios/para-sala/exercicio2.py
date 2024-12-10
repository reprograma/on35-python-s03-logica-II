# 2. Faça um programa que mostre na tela uma pergunta de múltipla escolha, e que, a partir da resposta do usuário, 
# mostre na tela se ele acertou ou não.

def calculo(soma):
    if soma == 'D' or soma == '4':
        return 'Parabéns! Você acertou!'
    else:
        return 'Hummm!!! Que pena você errou. Teremos laço apenas na próxima aula rs\n Semana que vem você tenta novamente rs'

pergunta_multipla_escolha = input("Quanto é 2 + 2? \n\n A) 0 \n B) 1 \n C) 2 \n D) 4 \n\n")
resultado = print(calculo(pergunta_multipla_escolha))

