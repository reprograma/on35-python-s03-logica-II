# 4. Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, pergunte quantos e mostre na tela uma mensagem de sua escolha.
# No caso de o usuário responder “não”, pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.

tem_irmaos = input("Você tem irmãos? ").lower()


def irmaos(tem_irmaos):
    if tem_irmaos == "sim":
        quantos_irmaos = input("Quantos irmãos você tem? ")
        return "Que a paciência esteja com você!"
    elif tem_irmaos == "não":
        queria_ter_irmaos = input("Gostaria de ter irmãos? ").lower()
        if queria_ter_irmaos == "sim":
            return "Cuidado com o que deseja kkk"
        else:
            return "Boa escolha!"
    else:
        return "Resposta inválida"


resposta = irmaos(tem_irmaos)

print(resposta)
