idade = int(input("insira sua idade: "))

if idade >= 18:
    print("Acesso liberado para compras 18+")
elif idade == 17:
    print("Logo você poderá comprar")
else:
    print("Acesso negado")

# if é a primeira condição, else é a condição se a if é falsa e o elif é como se fosse um if + else.
# == significa que não queremos atribuir o 17 a idade e sim comparar, então usamos o == para avisar o python que é uma comparação e não que é o valor.
# elif é como se fosse mais uma tratativa do if, tipo: se não é if, pode ser elif, e por fim vai vai ter o else.
# pode ter mais de um elif.

def verifica_idade(idade):
    if idade >= 18:
        return 'Acesso permitido para compras 18+'
    elif idade == 17:
        return 'Logo você poderá comprar'
    else:
        return 'Acesso negado'

idade_inserida = int(input("insira sua idade: "))
resultado = verifica_idade(idade_inserida)

print(resultado)

def tem_irmaos(resposta):
    if resposta == 'sim':
        print ('Que legal, você tem irmaos')
    elif resposta == 'não':
        print ('Entendi, você não tem irmaos')
    else:
        print ('Não entendi sua resposta')  

resposta_inserida = input('Você tem irmaos: ')
resultado = tem_irmaos(resposta_inserida)

print (resultado)

# Uso do print direto na função: limita o resultado, a função só vai printar o que foi feito no momento.
# Uso do retorn na função: pode usar em outros momentos e dai criar o resultado com o print. 
# mesmo exemplo de cima com o returno.

def tem_irmaos(resposta):
    if resposta == 'sim':
        return 'Que legal, você tem irmaos'
    elif resposta == 'não':
        return 'Entendi, você não tem irmaos'
    else:
        return 'Não entendi sua resposta'  

resposta_inserida = input('Você tem irmaos: ')
resposta_elaborada = print (f"Sua resposta é: {tem_irmaos(resposta_inserida)}")

