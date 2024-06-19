#4. Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, pergunte quantos 
# e mostre na tela uma mensagem de sua escolha. 
# No caso de o usuário responder “não”, pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.

irmaos = input("Você tem irmãos? s/n ")

if irmaos == "s":
    quantos_irmaos = input("Quantos irmãos você possui? ").lower()
    print(f"Que legal! Você tem {quantos_irmaos} irmãos.")
elif irmaos == "n":
    gostaria_irmaos = input("Você gostaria de ter irmãos? (s/n): ").lower()
    if gostaria_irmaos == "s":
        print("É muito bom ter irmãos, espero que um dia você tenha!")
    else:
        print("Tudo bem, ser filho único é ótimo também")
else:
    print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")