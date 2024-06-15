# 1. Faça um programa que peça para o usuário inserir uma idade e 
# mostre na tela se ele é maior de idade ou não.

idade = int (input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade")

elif idade < 18:  # porque usar elif e não o else?
    print("Menor de idade")
  

#2. Faça um programa que mostre na tela uma pergunta de múltipla escolha, 
# e que, a partir da resposta do usuário, mostre na tela se ele acertou ou não.

print ("Qual minha cor preferida?")
print ('A Azul')
print ('B Branco')
print ("C Amarelo")

resposta= str(input("A, B ou C?:")) 

if resposta=="A":
    print("Isso mesmo") #não ta printando

elif resposta=="B" or "C":  
    print("Dessas três cores, a que mais gosto é a Azul")


#3. Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, 
# em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.

nome = str(input("Digite seu nome: "))
gosta_nome =str(input("Você gosta do seu nome? Responda sim ou não?"))

if gosta_nome=="sim":
    print("Que maravilha") 

elif gosta_nome=="não":  
    print("Que pena")


#4. Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, 
# pergunte quantos e mostre na tela uma mensagem de sua escolha. No caso de o usuário responder “não”, 
# pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.

irmaos=str(input("Você tem irmãos ou irmãs? Responda sim ou não?"))
if irmaos=="sim":
    sim=str(input("Quantos?"))
    print("Que legal, também queria ter mais irmãos!") 

elif irmaos=="não":  
    nao=str(input("Voce gostaria de ter?"))  # aqui deveria colocar a opção caso seja sim ou não?
    print("Eu gosto de ser filha única!") 
   

#5. Faça um programa que permita o usuário escolher entre três opções de bebidas 
# e mostre na tela a bebida escolhida.

print ("Qual dessas bebidas você mais gosta?")
print ('A - Chá')
print ('B - Suco de frutas')
print ("C - café")

resposta= str(input("Escolha A, B ou C:")) 

if resposta=="A" or resposta=="Chá" or resposta=="a":
    print (resposta)
    print("Um chá antes de dormir é uma delícia") 

elif resposta=="B" or resposta=="Suco de frutas" or resposta=="b":
    print (resposta)  
    print("Você sabia que após alguns minutos de batido, o suco de frutas perde seus nutrientes?")

elif resposta=="C" or resposta=="Café" or resposta=="c":
    print (resposta)
    print("Ahhh adoro um cafezinho!")