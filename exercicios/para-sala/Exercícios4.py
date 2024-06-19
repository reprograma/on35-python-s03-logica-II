#Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, pergunte quantos e mostre na tela uma mensagem de sua escolha. No caso de o usuário responder “não”, pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.


def irmao(tem_irmao_pergunta):
    if tem_irmao_pergunta.lower() == 'sim':
        return ('Que legal!!' + (quantos_irmãos))
    elif tem_irmao_pergunta.lower() == 'não' or tem_irmao_pergunta.lowe() == 'nao':
        print (f'Que pena!'(gostaria_de_ter))


tem_irmao_pergunta = input('Tem irmãos?')
print (tem_irmao_pergunta)
quantos_irmãos = float(input('Quantos?'))
gostaria_de_ter = (input('Gostaria de ter irmãos?'))

irmao(tem_irmao_pergunta)





    

    
