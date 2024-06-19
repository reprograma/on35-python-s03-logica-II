def verifica_idade(idade):
if idade >= 18:
    return 'Acesso liberado para compras 18+'
elif idade == 17:
    return 'Logo você poderá comprar'
else: 
    return 'Acesso negado'

idadeInserida = int(input('Insira a idade da pessoa 1: '))
resultado = verifica_idade(idadeInserida1)

idadeInserida2 = int(input('Insira a idade da pessoa2: '))
resultado2 = verifica_idade(idadeInserida2)

print(f"pessoa 1: {resultado1}")
print(f"pessoa 2: {resultado2}")
