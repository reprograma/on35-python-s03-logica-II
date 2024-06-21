#2. Faça um programa que mostre na tela uma pergunta de múltipla escolha, 
# e que, a partir da resposta do usuário, mostre na tela se ele acertou ou não.

print ("Qual minha cor preferida?")
print ('A Azul')
print ('B Branco')
print ("C Amarelo")

resposta= str(input("A, B ou C?:")) 

if resposta=="A":
    print("Isso mesmo") #porque quando ta no arquivo com todos ele não retorna mas aqui ele ta retornando? tinha outro resposta na questao 4

elif resposta=="B" or "C":  
    print("Dessas três cores, a que mais gosto é a Azul")
