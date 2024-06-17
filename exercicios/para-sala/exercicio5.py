# Faça um programa que permita o usuário escolher entre três opções de bebidas e mostre na tela a bebida escolhida.

# opcoes_bebida = input('Qual bebida você deseja?\n a)Gin  b)Aguá  c)Vodka\nDigite sua resposta: ')
# bebida_escolhida = f'A sua bebida escolhida foi {opcoes_bebida}'
# print(bebida_escolhida)

def escolher_bebida(opcoes_bebida):
    if opcoes_bebida == 'gin': 
        return 'A sua bebida escolhida foi Gin'
    elif opcoes_bebida == 'aguá': 
        return 'A sua bebida escolhida foi Água'
    elif opcoes_bebida == 'vodka': 
        return 'A sua bebida escolhida foi Vodka'
    else:
        return 'Você não escolheu uma bebida válida'
    

opcoes_bebida = input('Qual bebida você deseja?\n a)Gin  b)Aguá  c)Vodka\nDigite sua resposta: ').lower()
print(escolher_bebida(opcoes_bebida))
