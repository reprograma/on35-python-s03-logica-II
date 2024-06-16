# Exercício: grupo 1

# ---------------------------------------------------------------------------------------------------------
# Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.
# ---------------------------------------------------------------------------------------------------------

# Opção 1

try:
  numero1 = int(input('Digite um Número: '))
  numero2 = int(input('Digite Outro Número: '))

  resultado_maior = numero1 > numero2
  resultado_igual = numero1 == numero2

  diferenca1 = numero1 - numero2
  diferenca2 = numero2 - numero1

  if resultado_maior == True and resultado_igual == False:
    print(f'O {numero1} é o maior dentre os números! E {numero1} - {numero2} = {diferenca1}')
  elif resultado_maior == False and resultado_igual == False:
    print(f'O {numero2} é o maior dentre os números! E {numero2} - {numero1} = {diferenca2}')
  else:
    print(f'Os números são iguais! E a diferença é 0!')
except:
  print('Por favor, digite um número inteiro!')

# Opção 2

def maior_e_diferenca(num1, num2):
    resultado_maior = num1 > num2
    resultado_igual = num1 == num2

    diferenca1 = num1 - num2
    diferenca2 = num2 - num1

    if resultado_maior == True and resultado_igual == False:
      print(f'O {num1} é o maior dentre os números! E {num1} - {num2} = {diferenca1}')
    elif resultado_maior == False and resultado_igual == False:
      print(f'O {num2} é o maior dentre os números! E {num2} - {num1} = {diferenca2}')
    else:
      print(f'Os números são iguais! E a diferença é 0!')
    
def solicitar_numeros():
  try:
    numero1 = int(input('Digite um Número: '))
    numero2 = int(input('Digite Outro Número: '))
    maior_e_diferenca(numero1,numero2)
  except:
    print('Por favor, digite um número inteiro!')
    
solicitar_numeros()

# ---------------------------------------------------------------------------------------------------------  
# Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".
# ---------------------------------------------------------------------------------------------------------

# Opção 1
try:
  numero1 = int(input('Digite um Número: '))
  numero2 = int(input('Digite Outro Número: '))

  if numero1 > numero2:
    print(f'Entre {numero1} e o {numero2}, o {numero1} é o maior!')
  elif numero2 > numero1:
    print(f'Entre {numero1} e o {numero2}, o {numero2} é o maior!')
  else:
    print(f'Números iguais!')
except:
  print('Por favor, digite um número inteiro!')

# Opção 2
def maior_igual(numero1, numero2):
  if numero1 > numero2:
    print(f'Entre {numero1} e o {numero2}, o {numero1} é o maior!')
  elif numero2 > numero1:
    print(f'Entre {numero1} e o {numero2}, o {numero2} é o maior!')
  else:
    print(f'Números iguais!')
    
def digitar_numeros():
  try:
    num1 = int(input('Digite um Número: '))
    num2 = int(input('Digite Outro Número: '))    
    maior_igual(num1, num2)
  except:
    print('Por favor, digite um número inteiro!')

digitar_numeros()

# ---------------------------------------------------------------------------------------------------------
# Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.
# ---------------------------------------------------------------------------------------------------------

# Opção 1
try:
  print('--------Dia da Semana--------')

  dia_da_semana = int(input('Digite um Número Inteiro de 1 a 7: '))
  
  if dia_da_semana >= 1 and dia_da_semana <= 7:
    if dia_da_semana == 1:
      print(f'{dia_da_semana} corresponde ao dia da semana Domingo!')
    elif dia_da_semana == 2:
      print(f'{dia_da_semana} corresponde ao dia da semana Segunda-feira!')
    elif dia_da_semana == 3:
      print(f'{dia_da_semana} corresponde ao dia da semana Terça-feira!')
    elif dia_da_semana == 4:
      print(f'{dia_da_semana} corresponde ao dia da semana Quarta-feira!')  
    elif dia_da_semana == 5:
      print(f'{dia_da_semana} corresponde ao dia da semana Quinta-feira!')    
    elif dia_da_semana == 6:
      print(f'{dia_da_semana} corresponde ao dia da semana Sexta-feira!')      
    else:
      print(f'{dia_da_semana} corresponde ao dia da semana Sábado!')
  else:
    print('Digite um número Inteiro entre 1 e 7!')
except:
  print('Por favor, digite um número inteiro entre 1 e 7!')
  
# Opção 2

def digite_dia(dia_da_semana):
  if dia_da_semana >= 1 and dia_da_semana <= 7:
    if dia_da_semana == 1:
      print(f'{dia_da_semana} corresponde ao dia da semana Domingo!')
    elif dia_da_semana == 2:
      print(f'{dia_da_semana} corresponde ao dia da semana Segunda-feira!')
    elif dia_da_semana == 3:
      print(f'{dia_da_semana} corresponde ao dia da semana Terça-feira!')
    elif dia_da_semana == 4:
      print(f'{dia_da_semana} corresponde ao dia da semana Quarta-feira!')  
    elif dia_da_semana == 5:
      print(f'{dia_da_semana} corresponde ao dia da semana Quinta-feira!')    
    elif dia_da_semana == 6:
      print(f'{dia_da_semana} corresponde ao dia da semana Sexta-feira!')      
    else:
      print(f'{dia_da_semana} corresponde ao dia da semana Sábado!')
  else:
    print('Digite um número Inteiro entre 1 e 7!')  
    
def solicitar_dia():
  try:
    print('--------Dia da Semana--------')

    dia_da_semana = int(input('Digite um Número Inteiro de 1 a 7: '))
    digite_dia(dia_da_semana)
  except:
    print('Por favor, digite um número inteiro entre 1 e 7!')

solicitar_dia()
  
# Exercício: grupo 2

# ---------------------------------------------------------------------------------------------------------
#Faça um programa que mostre ao usuario um menu com 4 opções de operações matemáticas (as básicas, por exemplo). O usuário escolhe uma das opçõoes e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado.
# ---------------------------------------------------------------------------------------------------------

# Opção 1

try:   
  print('---- Operações Matemáticas ----')
  print('1 - Somar')
  print('2 - Subtrair')
  print('3 - Multiplicar')
  print('4 - Dividir')
  
  escolha = int(input('Escolha uma das opções acima: '))   
  if escolha >= 1 and escolha <=4:  
    
    num1 = int(input('Agora Digite um Número: '))
    num2 = int(input('Digite outro Número: '))
      
    if escolha == 1:
      soma = num1 + num2
      print(f'A soma entre {num1} e {num2} é {soma}!')
    elif escolha == 2:
      subtracao = num1 - num2
      print(f'A subtração entre {num1} e {num2} é {subtracao}!')
    elif escolha == 3:
      multiplicacao = num1 * num2
      print(f'A multiplicação entre {num1} e {num2} é {multiplicacao}!')
    else:
      divisao = num1 / num2
      print(f'A divisão entre {num1} e {num2} é {divisao}!')
  else:
    print('Digite um número inteiro entre 1 e 4!')  
except:
  print('Digite números inteiros!')
  
# Opção 2

def escolha_num(escolha,num1,num2):    
  if escolha == 1:
    soma = num1 + num2
    return f'A soma entre {num1} e {num2} é {soma}!'
  elif escolha == 2:
    subtracao = num1 - num2
    return f'A subtração entre {num1} e {num2} é {subtracao}!'
  elif escolha == 3:
    multiplicacao = num1 * num2
    return f'A multiplicação entre {num1} e {num2} é {multiplicacao}!'
  else:
    divisao = num1 / num2
    return f'A divisão entre {num1} e {num2} é {divisao}!'

def escolha():
  print('---- Operações Matemáticas ----')
  print('1 - Somar')
  print('2 - Subtrair')
  print('3 - Multiplicar')
  print('4 - Dividir') 
  
  try:
    opcao = int(input('Escolha uma das opções acima: '))  
    if opcao >= 1 and opcao <=4:       
      num1 = int(input('Agora Digite um Número: '))    
      num2 = int(input('Digite outro Número: '))
      resultado = escolha_num(opcao,num1,num2)
      return resultado      
    else:
      return 'Digite um número inteiro entre 1 e 4!'
  except ValueError:
    return 'Digite números inteiros!'

print(escolha())
  
# ---------------------------------------------------------------------------------------------------------
# Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5, mas não simultaneamente pelos dois.
# ---------------------------------------------------------------------------------------------------------

# Opção 1

try:  
  num1 = int(input('Digite um número: '))
  if num1 % 3 == 0 and num1 % 5 == 0:
    print('Digite um número divisível por 3 ou 5')
  elif num1 % 3 == 0 or num1 % 5 == 0:
    if num1 % 3 == 0:
      print(f'{num1} é divisível por 3!')
    else:
      print(f'{num1} é divisível por 5!')
  else:
    print(f'{num1} não é divisivel nem por 3 nem por 5!')    
except:
  print('Digite números inteiros!')

# Opção 2

def divisivel(num1): 
  if num1 % 3 == 0 and num1 % 5 == 0:
    return 'Digite um número divisível por 3 ou 5'
  elif num1 % 3 == 0 or num1 % 5 == 0:
    if num1 % 3 == 0:
      return f'{num1} é divisível por 3!'
    else:
      return f'{num1} é divisível por 5!'
  else:
    return f'{num1} não é divisivel nem por 3 nem por 5!'    
    
def solicitar_num():
  try:    
    num1 = int(input('Digite um número: '))
    resultado = divisivel(num1)
    return resultado
  except ValueError:
    return 'Digite números inteiros!'

print(solicitar_num())
  
# Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou nao se aposentar. As condições para aposentadoria são:  • Ter pelo menos 65 anos, Ou ter trabalhado pelo menos 30 anos, Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos

# Oção 1

try:
  idade = int(input('Qual a sua idade? '))
  tempo = int(input('Há quantos anos você trabalha? '))
  
  if idade >= 65 or tempo >= 30:
    print('Parabéns! Você já pode se aposentar :)')
  elif idade >= 60 and tempo >= 25:
    print('Parabéns! Você já pode se aposentar :)')
  else:
    print('Você não pode se aposentar ainda! :(')
except:
  print('Digite números inteiros!')
  
# Opção 2
  
def aposenta_ou_nao(idade,tempo):
  if idade >= 65 or tempo >= 30:
    return 'Parabéns! Você já pode se aposentar :)'
  elif idade >= 60 and tempo >= 25:
    return 'Parabéns! Você já pode se aposentar :)'
  else:
    return 'Você não pode se aposentar ainda! :('

def idade_tempo():
  try:
    idade = int(input('Qual a sua idade? '))
    tempo = int(input('Há quantos anos você trabalha? '))
    resultado = aposenta_ou_nao(idade,tempo)
    return resultado
  except:
    return 'Digite números inteiros!'

print(idade_tempo())
