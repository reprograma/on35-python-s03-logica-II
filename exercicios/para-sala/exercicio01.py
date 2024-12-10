##Exercício de Sala 🏫
## 1 Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.


try:
    idade = int(input("Informe sua idade: "))
    if idade >= 18:
        print(f"O usuário tem {idade} anos, e é maior de idade.")
    else:
        print(f"O usuário tem {idade} anos, e é menor de idade.")
except ValueError:
    print("Dado incorreto")


##Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

 ##Fiz o fork do repositório.
 ##Clonei o fork na minha máquina (git clone url-do-meu-fork).
 ##Resolvi o exercício.
 ##Adicionei as mudanças. (git add . para adicionar todos os arquivos, ou git add nome_do_arquivo para adicionar um arquivo específico)
 ##Commitei a cada mudança significativa ou na finalização do exercício (git commit -m "Mensagem do commit")
 ##Pushei os commits na minha branch (git push origin nome-da-branch)