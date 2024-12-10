# Exercício de Sala 🏫  

#1. Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.

# Opçao 1

try:
  idade = int(input('Digite a sua idade: '))
  if idade >= 18 and idade < 123:
    print('Você é maior de idade!')
  elif idade >= 0 and idade < 123:
    print('Você não é maior de idade!')
  elif idade >= 123:
    print('Você seria maior de idade mas você ainda está vivo/a?\nA pessoa mais velha do mundo morreu com 122 anos!')
  else:
    print('Não existe idade negativa. Digite uma idade válida!')
except:
  print('Digite um numero inteiro!')
  
# Opçao 2

def maior_de_idade(idade):
  if idade >= 18 and idade < 123:
    return 'Você é maior de idade!'
  elif idade >= 0 and idade < 123:
    return 'Você não é maior de idade!'
  elif idade >= 123:
    return 'Você seria maior de idade mas você ainda está vivo/a?\nA pessoa mais velha do mundo morreu com 122 anos!'
  else:
    return 'Não existe idade negativa. Digite uma idade válida!'
    
def solicitacao_idade():
  try:
    num_idade = int(input('Digite a sua idade: '))
    resp = maior_de_idade(num_idade)
    return resp
  except:
    return 'Digite um numero inteiro!'

print(solicitacao_idade())

#2. Faça um programa que mostre na tela uma pergunta de múltipla escolha, e que, a partir da resposta do usuário, mostre na tela se ele acertou ou não.

# Opçao 1

try:
  print('-------- Comida Favorita --------')
  print('(1) Lasanha')
  print('(2) Moqueca')
  print('(3) Pizza')
  print('(4) Outra')    
  
  comida_favorita = int(input('Qual sua comida favorita?: '))
  if comida_favorita >= 1 and comida_favorita <= 4: 
    if comida_favorita == 1:
      print('Lasanha realmente é muito gostosa!')
    elif comida_favorita == 2:
      print('Moqueca é uma ótima opção!')    
    elif comida_favorita == 3:
      print('Pizza é uma opção maravilhosa para qualquer ocasião!')
    else:
      outra_comida = input('Me conta qual é: ')
      print(f'{outra_comida} é uma opção muito saborosa!')
  else:
     print('Escolha a opção entre 1 e 4!') 
except:
  print('Digite um número inteiro!')

# Opçao 2

def opcao_comida(comida_favorita):
  if comida_favorita >= 1 and comida_favorita <= 4: 
    if comida_favorita == 1:
      return 'Lasanha realmente é muito gostosa!'
    elif comida_favorita == 2:
      return 'Moqueca é uma ótima opção!'    
    elif comida_favorita == 3:
      return 'Pizza é uma opção maravilhosa para qualquer ocasião!'
    else:
      outra_comida = input('Me conta qual é: ')
      return f'{outra_comida} é uma opção muito saborosa!'
  else:
     return 'Escolha a opção entre 1 e 4!' 

def solicita_comida():
  try:
    print('-------- Comida Favorita --------')
    print('(1) Lasanha')
    print('(2) Moqueca')
    print('(3) Pizza')
    print('(4) Outra')    
    
    comida = int(input('Qual sua comida favorita?: '))
    resposta_comida = opcao_comida(comida)
    return resposta_comida
  except:
    return 'Digite um número inteiro!'
  
print(solicita_comida())

#3. Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.

# Opçao 1

nome = input('Insira um nome: ')
gosta = input('Você gosta do seu nome? (sim ou nao) ')

gosta_maiusc = gosta.upper()

if gosta_maiusc == 'SIM':
  print('Realmente! Esse nome é muito bonito!')
elif gosta_maiusc == 'NAO':
  print('Que pena! :(')
else:  
  print('Digite sim ou nao')

# Opçao 2

def gosta_ou_nao(gosta):
  gosta_maiusc = gosta.upper()

  if gosta_maiusc == 'SIM':
    return 'Realmente! Esse nome é muito bonito!'
  elif gosta_maiusc == 'NAO':
    return 'Que pena! :('
  else:  
    return 'Digite sim ou nao'
  
def solicita_nome():
  nome = input('Insira um nome: ')
  gosta = input('Você gosta do seu nome? (sim ou nao) ')
  sim_nao = gosta_ou_nao(gosta)
  return sim_nao

print(solicita_nome())

#4. Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, pergunte quantos e mostre na tela uma mensagem de sua escolha. No caso de o usuário responder “não”, pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.

# Opçao 1

pergunta = input('Você tem irmãos(as)? (sim/nao) ' )
pergunta_minusc = pergunta.lower()
if pergunta_minusc == 'sim':
  qtd = input('Quantos? ')
  print('Que legal! Crescer com ' + qtd + ' irmaos/as deve ser bem legal!')
elif pergunta_minusc == 'nao':
  quer_irmaos = input('Gostaria de ter? (sim/nao) ')
  quer_irmaos_minusc = quer_irmaos.lower()
  if quer_irmaos_minusc == 'sim':
    print('Você pode transferir seu amor e cuidado para seus/as primos/as ou amigos/as!')
  elif quer_irmaos_minusc == 'nao':
    print('Sua vontade foi realizada! Você é filha/o única/o!!')
  else:
    print('Digite sim ou nao') 
else:
  print('Digite sim ou nao')


# Opçao 2

def tem_irmao(pergunta):
  pergunta_minusc = pergunta.lower()
  if pergunta_minusc == 'sim':
    qtd = input('Quantos? ')
    return 'Que legal! Crescer com ' + qtd + ' irmaos/as deve ser bem legal!'
  elif pergunta_minusc == 'nao':
    quer_irmaos = input('Gostaria de ter? (sim/nao) ')
    quer_irmaos_minusc = quer_irmaos.lower()
    if quer_irmaos_minusc == 'sim':
      return 'Você pode transferir seu amor e cuidado para seus/as primos/as ou amigos/as!'
    elif quer_irmaos_minusc == 'nao':
      return 'Sua vontade foi realizada! Você é filha/o única/o!!'
    else:
      return 'Digite sim ou nao' 
  else:
    return 'Digite sim ou nao'

def pergunta_irmaos():
  pergunta = input('Você tem irmãos(as)? (sim/nao) ' )
  resposta = tem_irmao(pergunta)
  return resposta

print(pergunta_irmaos())

#5. Faça um programa que permita o usuário escolher entre três opções de bebidas e mostre na tela a bebida escolhida.

# Opçao 1

try:   
  print('---- Menu de Bebidas ----')
  print('(1) - Refri')
  print('(2) - Suco')
  print('(3) - Cerveja')
  
  escolha = int(input('Escolha uma das opções acima: '))   
  if escolha >= 1 and escolha <=3:        
    if escolha == 1:
      print('Refri é uma boa escolha :)')
    elif escolha == 2:
      print('Suco além de saudável é muito gostoso!')
    else:
      print('Cerveja é muito refrescante!')
  else:
    print('Digite um número inteiro entre 1 e 3!')  
except:
  print('Digite números inteiros!')
  
# Opçao 2

def opcoes_bebidas(escolha):
  if escolha >= 1 and escolha <=3:        
    if escolha == 1:
      return 'Refri é uma boa escolha :)'
    elif escolha == 2:
      return 'Suco, além de saudável, é muito gostoso!'
    else:
      return 'Cerveja é muito refrescante!'
  else:
    return 'Digite um número inteiro entre 1 e 3!' 
  
def escolha_bebida():
  try:   
    print('---- Menu de Bebidas ----')
    print('(1) - Refri')
    print('(2) - Suco')
    print('(3) - Cerveja')
    
    escolha_bebida = int(input('Escolha uma das opções acima: ')) 
    retorno = opcoes_bebidas(escolha_bebida)
    return retorno    
  except:
    return 'Digite números inteiros!' 
  
print(escolha_bebida())