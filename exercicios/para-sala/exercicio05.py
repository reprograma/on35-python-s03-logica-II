## 5 Faça um programa que permita o usuário escolher entre três opções de bebidas e mostre na tela a bebida escolhida.

def pedido(escolha):

    if  escolha == "agua" or escolha == "a)":
        return "A bebida escolhida foi agua"
    elif escolha == "suco" or escolha == "b)":
        return "A bebida escolhida foi suco"
    elif escolha == "refrigerante" or escolha == "c)":
        return "A bebida escolhida foi refrigerante"
    elif escolha == "cerveja" or escolha == "d)":
        return "A bebida escolhida foi cerveja"
    else:
        print("nenhuma bebida escolhida")


print("Cardapio bebidas",
      "a)agua",
      "b)suco",
      "C)refrigerante",
      "d)cerveja")
escolha_cardapio = input("escolha a bebida de sua preferenica:  ").lower()
print(pedido(escolha_cardapio))

##Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

 ##Fiz o fork do repositório.
 ##Clonei o fork na minha máquina (git clone url-do-meu-fork).
 ##Resolvi o exercício.
 ##Adicionei as mudanças. (git add . para adicionar todos os arquivos, ou git add nome_do_arquivo para adicionar um arquivo específico)
 ##Commitei a cada mudança significativa ou na finalização do exercício (git commit -m "Mensagem do commit")
 ##Pushei os commits na minha branch (git push origin nome-da-branch)