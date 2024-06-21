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



    # bebida=input ("Escolha uma bebida: \n a... coloque a letra da alternativa escolhida

Exercicio da colega corrigido:

    bebida = input("Escolha uma bebida: \n a - cerveja \n b - agua \n c - refrigerante \nEscolha uma das alternativas: ")
if bebida == 'a' or bebida == 'cerveja':
    print('Você escolheu cerveja')
elif bebida == "b" or bebida == 'agua':
    print('Você escolheu água')
elif bebida == 'c' or bebida == "refrigerante":
    print('Você escolheu refrigerante')
else:
    print("Resposta inválida")