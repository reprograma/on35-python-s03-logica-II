# Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou nao se aposentar. As condições para aposentadoria são: • Ter pelo menos 65 anos, • Ou ter trabalhado pelo menos 30 anos, • Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos
def calcula_aposentadoria(idade_trabalhador,tempo_servico):
    if (tempo_servico >= 25) and (idade_trabalhador >= 60):
        print('Trabalhador apto a se aposentar')
    elif idade_trabalhador >= 65:
        print('Trabalhador apto a se aposentar')
    elif tempo_servico >= 30:
        print('Trabalhador apto a se aposentar')
    else:
        print('Trabalhador ainda não pode se aposentar')
    

idade_trabalhador = int(input(('Insira a idade do trabalhador: ')))
tempo_servico = int(input(('Insira o tempo de servico do trabalhador: ')))
calcula_aposentadoria(idade_trabalhador,tempo_servico)