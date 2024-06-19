#Exercicio 1
#Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.

idade = int(input("Insira sua idade")) 
if idade >= 18: 
    print ("Você é maior de idade")
else: 
    print ("Você é menor de idade")

#Exercicio 2
#Faça um programa que mostre na tela uma pergunta de múltipla escolha, e que, a partir da resposta do usuário, mostre na tela se ele acertou ou não.

print ("Quanto é 1+2?")
print ("A-1; B-2.5; C-3")
resposta = input ("Selecione a resposta correta ")
if resposta == "C":
  print ("Parabéns! Você acertou.")
else:
  print ("Você errou. Tente novamente.")

#Exercicio 3
#Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.

nome = input ("Insira um nome")
resposta = input ("Você gosta do nome? Sim ou não? ")
if resposta == "Sim":
   print ("Que ótimo! Nós também gostamos do nome")
else:
   print ("Não é por nada não, mas nós também não curtimos o nome. Que tal escolher outro?")

#Exercicio 4
#4. Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, pergunte quantos e mostre na tela uma mensagem de sua escolha. No caso de o usuário responder “não”, pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.

print ("Você possui irmãos? ")
resposta = input ("Sim ou Não" )
if resposta == "Sim": 
   print ("Quantos irmãos você tem?")
   numero_irmaos = int(input())
   if numero_irmaos >= 1:
      print ("Que legal!")
else:
   print ("Você gostaria de ter irmãos?")
   respostadois = input ("Sim ou Não")
   if respostadois == "Sim":
    print ("Boa")
   else:
    print ("Que pena, amor")

#Exercicio 5
#Faça um programa que permita o usuário escolher entre três opções de bebidas e mostre na tela a bebida escolhida.

bebida = input ("Escolha entre Guaracamp, Coca-Cola e Convenção")
print ("A bebida escolhida foi ", bebida )

