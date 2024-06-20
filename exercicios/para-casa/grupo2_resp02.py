
def aposentadoria1(num1,num2):
    return num1>= 65 or num2 == 30

def aposentadoria2(num1,num2):
    return num1 == 60 and num2 == 25

idade=int(input("\nInforme sua idade: "))
tempo_servico=int(input("Informe o tempo de serviço: "))

if aposentadoria1(idade,tempo_servico):
    print("Pode se aposentar :)")

elif aposentadoria2(idade,tempo_servico):
    print("Pode se aposentar :)")
else:
        print("Não pode se aposentar :(")