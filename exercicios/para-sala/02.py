#Faça um programa que mostre na tela uma pergunta de múltipla escolha, e que, a partir da resposta do usuário, mostre na tela se ele acertou ou não.
print('Qual destas receitas é uma comida de origem italiana?')
print('a)pizza')
print('b)feijoada')
print('c)brigadeiro')

resposta = input('Escolha a opção correta (a, b ou c): ')
if resposta == 'a':
   print('Parabéns! Você acertou, Pizza é uma comida de origem italiana')
else: 
   print('Que pena! Resposta incorreta. A resposta correta é a) Pizza.')