# Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, 
# pergunte quantos e mostre na tela uma mensagem de sua escolha. No caso de o usuário responder “não”, 
# pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.


def tem_irmaos(resposta):
    if resposta == "Sim":
        quantos_irmaos = int(input("Quantos irmãos você tem? "))
        if quantos_irmaos == 1:
            return "Ah! Então você tem um irmão."
        elif quantos_irmaos > 1:
            return f"Nossa, então você tem {quantos_irmaos} irmãos!"
    

    elif resposta == "Não":
        decisao = input("Você gostaria de ter irmãos? (Sim/Não) ")
        if decisao == 'Sim':
            return "Ter irmãos te ensina várias coisas."
        elif decisao == "Não":
            return "Então você gosta de ser filho único."
        else:
            return "Resposta inválida. Por favor, responda 'Sim' ou 'Não'."

pergunta_irmaos = input("Você tem irmãos? (Sim/Não) ")
print(tem_irmaos(pergunta_irmaos))