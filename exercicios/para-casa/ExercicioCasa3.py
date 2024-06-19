def main():
    print("Escolha uma operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    
    escolhaNum = int(input("Digite o número da operação desejada: "))
    
    if escolhaNum not in range(1, 5):
        print("Opção inválida. Escolha um número entre 1 e 4.")
        return
    
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))
    
    if escolhaNum == 1:
        resultado = num1 + num2
    elif escolhaNum == 2:
        resultado = num1 - num2
    elif escolhaNum == 3:
        resultado = num1 * num2
    else:
        if num2 == 0:
            print("Não é possível dividir por zero.")
            return
        resultado = num1 / num2
    
    print(f"Resultado: {resultado:.2f}")

main()