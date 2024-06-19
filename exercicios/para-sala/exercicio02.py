## 2 Faça um programa que mostre na tela uma pergunta de múltipla escolha, e que, a partir da resposta do usuário, mostre na tela se ele acertou ou não.

def capital_do_brasil(resposta):
        
    if resposta == "c)brasilia" or resposta == "brasilia":
       return "Resposta certa"
    elif resposta == "c":
       return "Resposta certa"
    else:
       return "Resposta errada" 
    
      
print(" Qual a capital do brasil?",
          "\n a)São Paulo",
          "\n b)Rio de janeiro",
          "\n c)Brasilia")



resposta = input("Insira sua resposta:  ")
capital_do_brasil(resposta.lower())
 



##Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

 ##Fiz o fork do repositório.
 ##Clonei o fork na minha máquina (git clone url-do-meu-fork).
 ##Resolvi o exercício.
 ##Adicionei as mudanças. (git add . para adicionar todos os arquivos, ou git add nome_do_arquivo para adicionar um arquivo específico)
 ##Commitei a cada mudança significativa ou na finalização do exercício (git commit -m "Mensagem do commit")
 ##Pushei os commits na minha branch (git push origin nome-da-branch)