## 3 Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.

def pergunta(reposta,nome):

    if reposta == "sim":
       return f"Que legal! acho o nome {nome} lindo"
    else:
        return "E como você prefere ser chamada?"


nome_inserido = input("Insira seu nome:")
resposta_pergunta = input("Você gosta do seu nome?").lower()
print(pergunta(resposta_pergunta,nome_inserido))


##Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

 ##Fiz o fork do repositório.
 ##Clonei o fork na minha máquina (git clone url-do-meu-fork).
 ##Resolvi o exercício.
 ##Adicionei as mudanças. (git add . para adicionar todos os arquivos, ou git add nome_do_arquivo para adicionar um arquivo específico)
 ##Commitei a cada mudança significativa ou na finalização do exercício (git commit -m "Mensagem do commit")
 ##Pushei os commits na minha branch (git push origin nome-da-branch)