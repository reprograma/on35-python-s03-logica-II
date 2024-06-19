#Exercício de Casa 🏠 Grupo 2
## Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5, mas não simultaneamente pelos dois.

def verificar_divisibilidade(numero):

        if (numero % 3 == 0) and (numero % 5 == 0):
                print(f"{numero} essa operação nao é valida pois o numero escolhido é divisível por 3 e 5 ao mesmo tempo.")

        elif numero % 3 == 0:
                print(f"{numero} é divisível por 3, mas não por 5.")

        elif numero % 5 == 0:
                print(f"{numero} é divisível por 5, mas não por 3.")

        else:
                print(f"{numero} não é divisível nem por 3 nem por 5.")
                

def main():
    try:
        numero = int(input("Digite um número inteiro: "))
        verificar_divisibilidade(numero)
    except ValueError:
        print("Por favor, digite um valor inteiro válido.")

if __name__ == "__main__":
    main()