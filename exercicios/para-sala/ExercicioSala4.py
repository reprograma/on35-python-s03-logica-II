irmãosPergunta = input("Você tem irmãos? ").lower()

if irmãosPergunta == 's':
    irmãosQuantidade = input("Que legal, quantos irmãos você tem? ")
    print(f"Você tem {irmãosQuantidade} irmãos.")
elif irmãosPergunta == 'n':
    resposta = input("Você gostaria de ter irmãos? ")
    print(resposta)
    