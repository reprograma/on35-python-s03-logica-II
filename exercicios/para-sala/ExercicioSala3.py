nome = str(input("Digite um nome que você goste: "))

pergunta = str(input("Você gostou desse nome? ")).lower()

if pergunta == 's':
    print("Que bom de gostou!")
elif pergunta == 'n':
    print("Que pena que não gostou.")
