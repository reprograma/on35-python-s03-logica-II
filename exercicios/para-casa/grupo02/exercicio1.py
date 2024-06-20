def operacoes(resposta,numero1,numero2):
    if resposta == 'a':
        resultado = numero1 + numero2
        return f"O resultado da soma é: {resultado}"

    elif resposta == 'b':
        resultado =  numero1 - numero2
        return f"O resultado da subtração é: {resultado}"

    elif resposta == 'c':
       resultado= numero1 // numero2
       return f"O resultado da divisao é: {resultado}"

    elif resposta == 'd':
        resultado = numero1 * numero2
        return f"O resultado da multiplicação é: {resultado}"
    else:
        return "Operação inválida"
    

resposta = input('Escolha uma operação matemática: \na)adição\nb)subtração\nc)divisao\nd)multiplicação\n')
numero1 =int(input("Insira o primeiro número: "))
numero2 =int(input("Insira o segundo número: "))

print(operacoes(resposta,numero1,numero2))