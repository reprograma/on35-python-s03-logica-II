# 4. Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, pergunte quantos e mostre na tela uma mensagem de sua escolha. No caso de o usuário responder “não”, pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.
resposta = input("Você possui irmãos? (Sim ou Não): ")

if resposta.lower() == "sim":

    quantidade_de_irmãos = input("Que bom! Quantos irmãos você tem? ")
    print(f"Você tem {quantidade_de_irmãos} irmãos. Deve ser divertido!")
elif resposta.lower() == "não":
    gostaria_de_ter_irmãos = input("Que pena! Mas você gostaria de ter irmãos? (Sim ou Não): ")
    if gostaria_de_ter_irmãos.lower() == "sim":
        print("Entendi, seria legal ter irmãos para compartilhar momentos.")
    elif gostaria_de_ter_irmãos.lower() == "não":
        print("Entendo, cada um tem sua opinião.")
    else:
        print("Resposta inválida. Por favor, responda com 'Sim' ou 'Não'.")
