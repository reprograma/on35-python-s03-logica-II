# Lógica II

On35 | Semana 3 | 2024 | Agnes Ignácio

![enter image description here](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3h3YWVyaHppbG45bHh1ajl0aW13M3c5aHNta3VpdTVoODc1czFpbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8rleibGcxKqTC/giphy.webp)

### Instruções
Antes de começar, vamos organizar nosso setup.
* Fork esse repositório 
* Clone o fork na sua máquina (Para isso basta abrir o seu terminal e digitar `git clone url-do-seu-repositorio-forkado`)
* Entre na pasta do seu repositório (Para isso basta abrir o seu terminal e digitar `cd nome-do-seu-repositorio-forkado`)

### Resumo
O que veremos na aula de hoje?
* Condicionais
* Erros
* Debugger
* try - except

### Condicionais
As condicionais em Python são estruturas fundamentais na programação que permitem que um programa tome decisões com base em condições específicas. Em termos simples, as condicionais são usadas para controlar o fluxo de execução de um programa, permitindo que diferentes ações sejam tomadas dependendo de certas condições.

#### If - Else
Em Python, existem dois tipos principais de condicionais: o “if” e o “else”. O “if” é usado para verificar uma condição e executar um bloco de código se essa condição for verdadeira. Já o “else” é usado em conjunto com o “if” e permite executar um bloco de código alternativo caso a condição do “if” seja falsa.

#### Elif
Além disso, o Python também possui a estrutura “elif”, que significa “else if” e é usada para verificar múltiplas condições em sequência. Isso permite que um programa execute diferentes blocos de código dependendo de várias condições diferentes.

```
if afirmacao_logica:
  codigo_a_ser_executado
elif outra_afirmacao_logica:
  outro_codigo_a_ser_executado
else:
  codigo_final_a_ser_executado
```

### Erros
Você já deve ter percebido que os erros são muito comuns quando a gente vai lidar com tecnologia, né? Ao invés de nos estressarmos, vamos tentar entender os tipos de erros que podem acontecer e como solucionar cada um deles?

#### De Sintaxe
Esses são os mais comuns. São erros em que nós escrevemos o código de forma incorreta e, por isso, o Python não consegue entender o que queremos dizer. Em geral, esses erros vão quebrar o código imediatamente ao tentarmos rodá-lo e o terminal nos apontará o que aconteceu.
Exemplo de código que retornaria um erro de sintaxe:
```
def minha_funcao(meu_argumento:
print(meu_argumento)
```

Nesse exemplo, temos dois erros de sintaxe: não fechamos os parenteses ao definir o argumento da nossa função e não demos identação no conteúdo da função.

#### De Execução
São erros em que nós escrevemos o nosso código com a sintaxe correta, porém tentamos fazer algo que o Python não é capaz de fazer. Um exemplo clássico é quando tentamos dividir algum número por 0:
```
num1 = 0
num2 = 3
print(num2/num1)
```

Nesse caso, ao tentar rodar esse código, nosso terminal retornaria um erro avisando que a divisão por 0 é uma operação impossível para o Python.

#### Semânticos
Enquanto os de sintaxe são erros de escrita, os semânticos são erros de significado. Neles, nosso código vai rodar normalmente, sem sinalizar nenhum problema. Porém, ao observarmos o resultado, veremos que não é o esperado. Isso provavelmente significa que na hora de construir nosso raciocínio, falhamos em alguma etapa lógica ou ao tentar traduzí-la para Python. Este tipo de erro é o mais complexo de identificar e demanda uma ferramenta incrível chamada Debugger.

### Debugger
O Debugger é a nossa ferramenta de depuração. Depuração corresponde ao processo de localizar e corrigir erros ou bugs no código-fonte de qualquer software. Quando o software não funciona conforme o esperado, as programadoras de computadores estudam o código para determinar as causas dos erros. Elas usam ferramentas de depuração para executar o software em um ambiente controlado, verificar o código detalhado, e analisar e corrigir o problema.

O termo “debugging” (depuração) remonta à almirante Grace Hopper, que trabalhou na Harvard University na década de 1940. Quando um de seus colegas encontrou uma mariposa impedindo o funcionamento de um dos computadores da universidade, ela disse que eles estavam “debugging” o sistema. Os primeiros registros de programadores de computadores usando os termos “bugs” e “debugging” data a década de 1950. No início da década de 1960, esses termos já eram comumente aceitos na comunidade de programação.

Bugs e erros acontecem na programação de computadores porque é uma atividade abstrata e conceitual. Os computadores manipulam dados na forma de sinais eletrônicos. As linguagens de programação abstraem essas informações para que os humanos possam interagir com os computadores de forma mais eficiente. Quaisquer tipos de softwares possuem diversas camadas de abstração com diferentes componentes que se comunicam para que uma aplicação funcione adequadamente. Quando ocorrem erros, encontrar e resolver o problema pode ser um desafio. As ferramentas e estratégias de depuração ajudam a corrigir problemas mais rapidamente e melhoram a produtividade do desenvolvedor. Como resultado, a qualidade do software e a experiência do usuário final são melhoradas.

### try - except
O Try Except é uma construção fundamental na linguagem de programação Python para lidar com exceções e erros. Ele permite que o desenvolvedor controle o fluxo do programa e trate de forma adequada as situações inesperadas que possam ocorrer durante a execução do código. Quando sabemos que determinados erros podem acontecer, inserimos o código dentro de try - except para dizer ao Python o que fazer quando o erro acontece. Por exemplo:

```
try:
  num1 = float(input('insira o primeiro número: ')
  num2 = float(input('insira o segundo número: ')

  media = (num1 + num2) / 2
  print(f"Sua média foi {media}")
except:
  print('número inserido inválido')
```

No exemplo, usamos o try - except para prever a possibilidade da pessoa usuária inserir caracteres que não são números no terminal. No bloco de código sob try, indicamos a operação a ser feita. Sob o except, indicamos o que deve acontecer caso o código retorne um erro.

Os blocos except podem ter erros específicos a serem cobertos. Se atualizarmos nosso exemplo, teriamos algo como:
```
try:
  num1 = float(input('insira o primeiro número: ')
  num2 = float(input('insira o segundo número: ')

  media = (num1 + num2) / 2
  print(f"Sua média foi {media}")
except ValueError:
  print('número inserido inválido')
```

Nesse caso, específicamos para o Python que, ao ocorrer um ValueError, a resposta é o bloco except. Se qualquer outro erro ocorrer, ele não estará coberto pelo try - except. Para cobrir todas as possibilidades, usamos o except sem especificação, como no primeiro exemplo.

### Links úteis
* [Condicionais](https://awari.com.br/condicionais-python-aprenda-a-utilizar-estruturas-condicionais-em-python/)
* [O que é depuração? - AWS](https://aws.amazon.com/pt/what-is/debugging/#:~:text=Depura%C3%A7%C3%A3o%20corresponde%20ao%20processo%20de,determinar%20as%20causas%20dos%20erros.)
* [try - except](https://awari.com.br/python-aprenda-a-usar-o-try-except-para-lidar-com-erros/)
