# * Faça um programa que mostre ao usuario um menu com 4 opções de operações matemáticas (as básicas, por exemplo).
# O usuário escolhe uma das opçõoes e o seu programa então pede dois valores numéricos e realiza a operação, 
# mostrando o resultado.

def calculadora():
    escolha_operacao = int(input("Escolha uma das operações abaixo para realizar o seu calculo:\n"
        "1.soma \n"
        "2.subtração \n"
        "3.multiplicação \n"
        "4.divisão = 4 : \n"))
    
    informe_n1 = float(input("Informe um número1? : "))
    informe_n2 = float(input("Informe um número2? : "))


    if escolha_operacao == 1:
        return informe_n1 + informe_n2

    elif escolha_operacao == 2 :
        return informe_n1 - informe_n2

    elif escolha_operacao == 3:
            return informe_n1 * informe_n2

    elif escolha_operacao == 4:
        return  informe_n1 / informe_n2
    
    else:
        return "Operação invalida"



print(calculadora())