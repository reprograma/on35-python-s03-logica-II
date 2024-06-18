# 2.Faça um programa que mostre na tela uma pergunta de múltipla escolha, e que, a partir da resposta do usuário, mostre na tela se ele acertou ou não.

def multiplaEscolha (pergunta):
    if pergunta == 'c':
        return 'Paraaaabéns, você A R R A Z A\nA pessoa inventora do Chuveiro Elétrico é do Braaaasil!\nFrancisco Canhos é o nome do homem que, na década de 40, desenvolveu o primeiro chuveiro elétrico seguro em Jaú-SP. O aparelho vinha sendo desenvolvido desde os anos 30, mas apresentava riscos de curto-circuito.'
    else:
        return'Poxa, não foi dessa vez! Continue tentando <3'

digiteAlternativa = str(input('De onde é a pessoa que inventou o chuveiro elétrico?\na) França\nb) Inglaterra\nc) Brasil\nd) Austrália\ne) Itália\nDigite a alternativa: ')).lower()
resultado_opcao = multiplaEscolha(digiteAlternativa)

print(resultado_opcao)