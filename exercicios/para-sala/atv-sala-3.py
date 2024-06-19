#Aluna: Karine Lessa
#Dia: 15/06/2024


# Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.

idade = int(input("Insira sua idade aqui, por gentileza: "))

if idade >= 18:
    print("Maior de idade, ihul!")
else:
    print("Sinto muito, você não é maior de idade.")

#Faça um programa que mostre na tela uma pergunta de múltipla escolha, e que, a partir da resposta do usuário, mostre na tela se ele acertou ou não.


pergunta = "Qual é a bandeira mais bonita do Brasil?"
print(pergunta)
opcoes = ["a) Rio de Janeiro', 'b) São Paulo', 'c) Alagoas', 'd)Pernambuco" ]
print(opcoes)
resposta_correta = 'd'



resposta = input("Escolha a resposta correta (a/b/c/d): ")

if resposta == resposta_correta:
    print("Acertou, mulher!")

else:
    print(f"Errou feio, gata! A resposta correta é {resposta_correta} - Pernambuco.")



#Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.

nome = input("Insira o seu nome: ")

voce_gosta_do_nome = input("Você gosta do seu nome? (Sim/Não): ")

if voce_gosta_do_nome == "sim" or voce_gosta_do_nome == "Sim" or  voce_gosta_do_nome == "SIM":
    print (f"Massaa! Fico feliz que você gosta do seu nome,{nome}!")
else:
    print(f"Ah, que pena! Sinto muito que você não gosta do seu nome,{nome}.")

#Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, pergunte quantos e mostre na tela uma mensagem de sua escolha. No caso de o usuário responder “não”, pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.

tem_irmaos = input("Você possui irmãos? (Sim/Não): ")

if tem_irmaos == "sim" or tem_irmaos == "Sim" or tem_irmaos == "SIM":
    quantidade = int(input("Quantos irmãos você tem? "))
    print(f"Que legal! Você tem {quantidade} irmão(s).")
else:
    gostaria = input("Você gostaria de ter irmãos (Sim/Não): ")
    if gostaria == "sim" or gostaria == "Sim" or gostaria == "SIM":
        print("Ah, entendi! Espero que um dia você possa.")
    else:
        print("Ok, meu bem! sem problemas.")

 #Faça um programa que permita o usuário escolher entre três opções de bebidas e mostre na tela a bebida escolhida.

bebidas = {
    1: "Água",
    2: "Caipirinha",
    3: "Alcatrão com mel e limão",
    4: "Cerveja"
}
print("Escolha uma bebida:")
print("1) Água")
print("2) Caipirinha")
print("3) Alcatrão com mel e limão")
print("4) Cerveja")

escolha = int(input("Digite o número da sua bebida favorita:"))

if escolha in bebidas:
    print(f"Que delícia, eu também amo essa! {bebidas[escolha]} é ótimo")
else:
    print("Essa opção não está disponível, tente novamente!")

