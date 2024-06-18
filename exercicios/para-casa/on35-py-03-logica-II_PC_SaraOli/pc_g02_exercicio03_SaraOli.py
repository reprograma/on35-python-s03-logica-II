#Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou nao se aposentar. As condições para aposentadoria são:
#  • Ter pelo menos 65 anos,
#  • Ou ter trabalhado pelo menos 30 anos,
#  • Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos

def previdencia():
    idade = float(input('Olá, vamos realizar o cálculo para saber se você já tem direito de solicitar sua aposentadoria e/ou quanto tempo falta.\nPara iniciarmos, por favor, digita para mim sua idade: '))
    tempoDeContribuicao = float(input('Insira o período total, em anos, de contribuição: '))
    identidade_genero = input('Desculpe, mas precisamos solicitar essa informação, pois o regime previdenciário possui regras diferentes para cada gênero.\nVocê se identifica com qual gênero (feminino, masculino ou outros)? ').lower()

    if identidade_genero == 'f' or identidade_genero == 'feminino':
        if idade >= 60 and tempoDeContribuicao >= 25:
            print(f"Parábens, com {idade} de idade e {tempoDeContribuicao} anos de contribuição, você já é elegível para se aposentar! Entre em contato com o INSS da sua região :)")
        else:
            if idade < 60:
                print(f"Você ainda não está elegível para se aposentar, porque sua idade de {idade} é menor que 60 anos.")
            elif tempoDeContribuicao < 25:
                print(f"Você ainda não está elegível para se aposentar, porque seu tempo de contribuição {tempoDeContribuicao} é menor que 25 anos.")
                
    elif identidade_genero == 'm' or identidade_genero == 'masculino':
         if idade >= 65 and tempoDeContribuicao >= 30:
              print(f"Parábens, com {idade} de idade e {tempoDeContribuicao} anos de contribuição, você já é elegível para se aposentar! Entre em contato com o INSS da sua região :)")
         else:
            if idade < 65:
                print(f"Você ainda não está elegível para se aposentar, porque a idade de {idade} é menor que 65 anos.")
            elif tempoDeContribuicao < 30:
                print(f"Você ainda não está elegível para se aposentar, porque seu tempo de contribuição {tempoDeContribuicao} é menor que 30 anos.")

previdencia()