#1. Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.

idade = int(input("Insira sua idade -> "))

if idade >= 18:
    print("Você é maior de idade, ja pode dirigir e ingerir álcool com moderação :D")
elif idade < 18:
    print("Você é menor de idade, cuidado com a vida, ein!")
else:
    print("Não estamos te entendendo")





#2.Faça um programa que mostre na tela uma pergunta de múltipla escolha, e que, a partir da resposta do usuário, mostre na tela se ele acertou ou não.

pergunta = input("Qual é o maior feito da carreira da Beyoncé?" "a) O Renaissence | b) O self title com um clipe por faixa | c) O Black IS King, do Rei Leão | d) O Beychella | e) O nascimento dela e tudo que aconteceu depois é a melhor coisa que aconteceu na história do mundo")

if pergunta == "a" or pergunta == "b" or pergunta == "c" or pergunta == "d":
    print("Esse é muito bom, mas a resposta não está completa :/")
elif pergunta == "e":
    print("Acretou, beyfã" )
else:
    print("Responde direito, mulher!")





#3. Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.

nome = input("Me fala, qual o seu nome?")

voce_gosta = input("Você gosta dele? Responda com sim ou não.")

if voce_gosta == "Sim" or voce_gosta == "sim":
    print("Também gostei, é um nome bem bonito")
elif voce_gosta == "Não" or voce_gosta == "não":
    print("Caramba, eu gostei dele. Meu nome é Xainã e eu costumava não gostar dele, mas agora eu amo.")
else:
    print ("Não entendi a sua resposta :/")





#4. Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, pergunte quantos e mostre na tela uma mensagem de sua escolha. No caso de o usuário responder “não”, pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.

tem_irmao = input("Você tem algum irmão ou irmã? Responda com sim ou não.")

if tem_irmao == "sim" or tem_irmao == "Sim":
    print(input("Quantos irmãos?")) ##como fazer pra dar uma resposta independente da resposta?
elif tem_irmao == "não" or tem_irmao== "Não":
    print(input("Mas você gostaria de ter?"))
else:
    print("Não entedi sua resposta")




#5. Faça um programa que permita o usuário escolher entre três opções de bebidas e mostre na tela a bebida escolhida.

print("Temos apenas 3 tipos de bebida: Pitu, Devassa e Chop de Vinho.")
bebida = input ("Dessas, qual você gostaria de tomar?")

if bebida == "pitu" or bebida == "Pitu":
    print("Certo, sua Pitu chega em 5 minutos")

elif bebida == "Devassa" or bebida == "devassa":
    print("Certo, vou pegar sua Devassa agora")

elif bebida == "Chop de Vinho" or bebida =="chop de vinho":
    print("Maravilha, seu Chop de Vinho chega em 5 minutos")
else:
    print(input("Não entendi sua resposta. Qual das bebidas você gostaria?")) ##como retornar para o input de cima?


#Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

#- [ ] Fiz o fork do repositório.
#- [ ] Clonei o fork na minha máquina (`git clone url-do-meu-fork`).
#- [ ] Resolvi o exercício.
#- [ ] Adicionei as mudanças. (`git add .` para adicionar todos os arquivos, ou `git add nome_do_arquivo` para adicionar um arquivo específico)
#- [ ] Commitei a cada mudança significativa ou na finalização do exercício (`git commit -m "Mensagem do commit"`)
#- [ ] Pushei os commits na minha branch (`git push origin nome-da-branch`)
