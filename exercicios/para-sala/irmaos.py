# 4. Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, 
# pergunte quantos e mostre na tela uma mensagem de sua escolha. No caso de o usuário responder “não”, 
# pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.


tem_irmaos = input("Voce têm irmaos? (sim/nao) : ")
if tem_irmaos == "sim":
    quantidade = (int(input("Quantos? :")))
    print(f"Eu tenho {quantidade} irmãos")
else:
    gostaria_de_ter = print(input("Gostaria de ter? (sim/nao) : "))
    if gostaria_de_ter == "sim":
        print("Eu gostaria de ter irmãos.")
    else:
        print("Eu não gostaria de ter irmãos.")
    
