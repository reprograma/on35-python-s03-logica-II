#Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.

def pergunta_nome(gostar_nome): 
    if gostar_nome.lower() == 'sim':
        print ('Que legal, seu nome é realmente lindo!')
    else: 
        print ('Poxa que pena!')
    
nome = input('Qual é o seu nome? ') 
gostar_nome = input('Você gosta do seu nome? (sim/não) ') 

pergunta_nome(gostar_nome)









