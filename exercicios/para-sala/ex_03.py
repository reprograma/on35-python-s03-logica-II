#3. Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, 
# em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.

nome = str(input("Digite seu nome: "))
gosta_nome =str(input("Você gosta do seu nome? Responda sim ou não?"))

if gosta_nome=="sim":
    print("Que maravilha") 

elif gosta_nome=="não":  
    print("Que pena")