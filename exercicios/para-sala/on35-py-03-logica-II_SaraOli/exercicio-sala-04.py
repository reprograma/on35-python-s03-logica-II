# 4.Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, pergunte quantos e mostre na tela uma mensagem de sua escolha. No caso de o usuário responder “não”, pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.

def temIrmaes (irmaes):
    if irmaes == 'Sim':
        irmaes =  int(input('Quantos, quantas ou quantes irmães você tem? '))
        return ('Wow, que massaaa! Ter irmães é bom demaaaais, não importa a quantidade =)')
    else:
        resposta_negativa = str(input('Você gostaria de ter irmães? '))
        if resposta_negativa == 'Não':
          return 'Entendi, gostei da sua franqueza! =)'
        else:
            return 'Tente não ficar chateade, existem laços de fraternidade consanguíneos que pode ser equivalente a esse ente querido :)'

pergunta_principal = str(input('Você tem irmães ? ')).capitalize()
print(temIrmaes(pergunta_principal))
''' 
resultado_irmaos = str(input('Você tem irmães? '))

resultado = temIrmaos(resultado_irmaos)

print(resultado)'''