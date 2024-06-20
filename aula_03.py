def tem_irmaos(resposta):
    if resposta == 'sim':
        return 'Que legal, você tem irmaos'
    elif resposta == 'nao':
        return 'Entendi, você nao tem irmaos'
    else:
        return 'nao entendi sua resposta'


respostaInserida = input('Você tem irmaos? ')
reposta_elaborada = print(f"Sua resposta é: {tem_irmaos(respostaInserida)}")