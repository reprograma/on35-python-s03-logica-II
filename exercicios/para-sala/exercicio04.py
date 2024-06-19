#Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, pergunte quantos e mostre na tela uma mensagem de sua escolha. No caso de o usuário responder “não”, pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.



def possui_irmaos(resposta):
    if resposta.lower () == "sim":
        quantos_irmaos = int(input("Entendi! Quantos irmãos você tem? "))
        if quantos_irmaos == 1:
            return "Entendi! Você tem 1 irmão"

        else:    return f"Entendi! Você tem {quantos_irmaos} irmãos."
    
    else:
        resposta_2 = input("Você gostaria de ter? ")
        if resposta_2.lower() == "sim":
            return "Agradecemos pela resposta"
        elif resposta_2.lower () == "não":
            return "Agradecemos pela resposta"

    
    
pergunta_irmaos = input("Você tem irmãos? ")
print(possui_irmaos(pergunta_irmaos))