#Faça um programa que mostre na tela uma pergunta de múltipla escolha, e que, 
# a partir da resposta do usuário, mostre na tela se ele acertou ou não.

def cor_bonita(resposta):
    if resposta == "B" or "b":
        return "Isso, eu também acho!"
    elif resposta == "A" or "C" or "D"or 'a' or 'c' or 'd':
        return "Poxa vida, faz parte mas não é a resposta certa!"
    
pergunta = input('Qual a cor mais bonita que existe?:   A/ azul B/ arco-iris C/ vermelho D/ amarelo:    ')
resultado_resp = cor_bonita(pergunta)

print(resultado_resp)


# Feito na correção, estudar mais




