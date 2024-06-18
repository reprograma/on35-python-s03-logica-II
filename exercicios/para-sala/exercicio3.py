# 3. Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, em ambos os possíveis casos de resposta (Sim ou Não),
# mostre uma mensagem de sua escolha na tela.

nome_inserido = input("Escreva um nome: ")
gosta_nome = input("Você gosta deste nome? ").lower()


def retorna_nome(nome):
    if gosta_nome == "sim":
        return "Que legal! Boa escolha."
    elif gosta_nome == "não":
        return "Poxa, que pena!"
    else:
        return "Não consegui entender sua resposta"


resposta = retorna_nome(nome_inserido)

print(resposta)
