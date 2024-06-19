#Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, 
#pergunte quantos e mostre na tela uma mensagem de sua escolha. No caso de o usuário responder “não”, 
#pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.

pergunta_sobre_irmaos = input("Você possui irmãos? ")

if pergunta_sobre_irmaos == "sim":
        quantos_irmaos = input("Quantos irmãos você tem? ")
        print (f"Que massaaaa!") 
elif pergunta_sobre_irmaos == "não":
    pergunta2 = input("Você gostaria de ter?")
    if pergunta_sobre_irmaos == "sim":
        print("Legal!")
    elif pergunta_sobre_irmaos == "não":
        print ("As vezes é bom mesmo ser filho único rs")
    else: 
        print("Favor responder com 'sim' ou 'não'")        


