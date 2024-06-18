# 1. Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.

def verificaIdade (idade):
    if idade >= 18:
        return 'Parabéns, você é maior de idade!'
    elif idade == 17:
        return 'Você ainda não chegou lá, mas em breve vocêalcançará a maioridade'
    else:
        return 'Falta mais tempo até você chegar, lá!'

digiteIdade = int(input('Insira sua idade para verificar maioridade: '))
resultado_idade = verificaIdade(digiteIdade)

print(resultado_idade)