
# Exercício de Sala 🏫 

#4. Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, pergunte quantos e mostre na tela uma mensagem de sua escolha. No caso de o usuário responder “não”, pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.

def pergunta_irmao():
    pergunta = input("Você tem irmão? (sim/não): ")

    if pergunta == "sim":
        quantidade_irmao = int(input("Quantos irmãos você tem? "))
        print(f"Que legal! Você tem {quantidade_irmao} irmão.")
    elif pergunta == "não":
        nao_tem_irmao = input("Gostaria de ter irmão? (sim/não): ")
        if nao_tem_irmao == "sim":
            print("Seria bom ter irmãos!.")
        else:
            print("Tudo bem, não tem problema.")
    else:
        print("Resposta inválida. Por favor, responda com 'sim' ou 'não'")


pergunta_irmao()

        



    

        
              

    