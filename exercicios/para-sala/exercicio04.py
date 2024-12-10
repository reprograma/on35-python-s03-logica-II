## 4 Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, pergunte quantos e mostre na tela uma mensagem de sua escolha. No caso de o usuário responder “não”, pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.
def tem_irmaos(resposta):
    
    if resposta == "sim":
        quantos_irmaos = int(input("Que legal! Quantos irmãos você tem? "))
        if quantos_irmaos == 1:
            return f"Que legal, você tem 1 irmão"
        else: 
            return f"Que legal!você tem {quantos_irmaos} irmãos."
              
    else:
            nao_tem_irmaos = input("você gostaria de ter?")
            if nao_tem_irmaos == "sim":
             return"Que legal! é muito bom ter irmãos"
            else:
             return"Obrigada pela resposta"


resposta_da_pergunta = input("Você tem irmãos? ").lower()
print(tem_irmaos(resposta_da_pergunta).lower())

##Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

 ##Fiz o fork do repositório.
 ##Clonei o fork na minha máquina (git clone url-do-meu-fork).
 ##Resolvi o exercício.
 ##Adicionei as mudanças. (git add . para adicionar todos os arquivos, ou git add nome_do_arquivo para adicionar um arquivo específico)
 ##Commitei a cada mudança significativa ou na finalização do exercício (git commit -m "Mensagem do commit")
 ##Pushei os commits na minha branch (git push origin nome-da-branch)