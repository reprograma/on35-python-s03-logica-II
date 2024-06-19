pergunta = "Quanto é 200/4?\n(a) 50\n(b) 30\n(c) 60\n(d) 40\n"

respostaCerta = "a"

resposta = input(pergunta).lower()

if resposta == respostaCerta:
    print("Resposta correta!")
else:
    print(f"Resposta incorreta. A resposta certa era letra a.")