#Faça um programa que mostre na tela uma pergunta de múltipla escolha, 
#e que, a partir da resposta do usuário, mostre na tela se ele acertou ou não.

pergunta = "Quais os estados estão localizados na região Norte do Brasil?"
opções = " A) Pará", "B) Manaus", "C) Tocantins", "D) Todas as alternativas estão corretas" 
resposta_correta = "D"

print(pergunta)
print (opções)

resposta_pessoa = input("Escolha a alternativa correta: ")

if resposta_pessoa == resposta_correta:
    print("Parabéns! Você acertou! :D")
else:
    print("Resposta incorreta :(")    
