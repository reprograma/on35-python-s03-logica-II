numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um segundo número: "))

if numero1 > numero2:
    print(f"O número maior é: {número1}")
    diferenca = numero1 - numero2

elif numero2 > numero1:
    print(f"O número maior é: {numero2}")
    diferenca = numero2 - numero1

else:
    print("Os dois números são iguais")
    diferenca = 0

print(f"A diferença entre os dois números é: {diferenca}")