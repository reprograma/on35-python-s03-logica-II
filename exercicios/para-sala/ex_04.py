#4. Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, 
# pergunte quantos e mostre na tela uma mensagem de sua escolha. No caso de o usuário responder “não”, 
# pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.

irmaos=str(input("Você tem irmãos ou irmãs? Responda sim ou não?")) #definir a função
if irmaos=="sim":
    sim=str(input("Quantos?"))
    print("Que legal, também queria ter mais irmãos!") #não usar o print e sim o return

elif irmaos=="não":  
    nao=str(input("Voce gostaria de ter?"))  # aqui deveria colocar a opção caso gostaria de ter ou não?
    print("Eu gosto de ser filha única!") 


    # na aula 
    #def tem_irmaos(resposta):
    #if resposta == 'sim':
        #return 'Que legal, você tem irmaos'
   # elif resposta == 'nao':
       # return 'Entendi, você nao tem irmaos'
    #else:
       # return 'nao entendi sua resposta'


#respostaInserida = input('Você tem irmaos? ')
#reposta_elaborada = print(f"Sua resposta é: {tem_irmaos(respostaInserida)}")

#corrigido da colega:

def tem_irmaos(resposta):
    if resposta == "Sim" or resposta == "sim":
       quantos_irmaos = int(input("Que legal! Quantos irmãos você tem? "))
       if quantos_irmaos == 1:
           return "Que legal! Você tem 1 irmão"
       else:
           return f"Que legal! Você tem {quantos_irmaos} irmãos."
       
    else:
        resposta_2 = input("Você gostaria de ter? ")
        if resposta_2 == "sim" or resposta_2 == "Sim":
            return "Agradecemos pela resposta"
        elif resposta_2 == "não" or resposta_2 == "Não":
            return "Agradecemos pela resposta"
       
  
    
    
pergunta_irmaos = input("Você tem irmãos? ")
print(tem_irmaos(pergunta_irmaos))