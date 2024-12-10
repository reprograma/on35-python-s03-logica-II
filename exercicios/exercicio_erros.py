nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))

media = (nota1+nota2) / 3


try:
    numero1 = 10
    numero2 = 0
    resultado = numero1/numero2

    print(resultado)
except ZeroDivisionError:
    print('Divisao por zero')

# com try a gente pode trazer erros que podem acontecer e tratar eles de forma antecipada, pro usuario final saber o que fazer.
# é possível colocar mais de um except.
# é possível colocar apenas except e ai ele vai puxar qualquer erro.


try:
    nota1 = float(input('Insira a primeira nota: '))
    nota2 = float(input('Insira a segunda nota: '))

    media = (nota1+nota2) / 2

    print(media)
except ValueError:
    print('Numero inserido invalido')
