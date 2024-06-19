# Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.

def numero_maior(numero1, numero2):
    if numero1 > numero2:
        diferenca = numero1 - numero2
        return f'{numero1} é maior que {numero2} e a diferença entre eles é {diferenca}'
    elif numero2 > numero1:
        diferenca = numero2 - numero1
        return f'{numero2} é maior que {numero2} e a diferença entre eles é {diferenca}'
    else: numero1 == numero2
    return f'Ambos os números são iguais e não possuem diferença'

primeiro_numero = int(input("Insira o primeiro número: "))
segundo_numero = int(input("Insira um segundo núnero: "))

resposta = (numero_maior(primeiro_numero, segundo_numero))
print(resposta)

                