#5.Faça um programa que permita o usuário escolher entre três opções de bebidas e 
# mostre na tela a bebida escolhida.

def escolhaBebidas ():
    armazena_lista = ['Erva Mate', 'Tererê', 'Chimarrão', 'Camomila', 'Hortelã', 'Boldo', 'Cidreira']
    
    opcao_bebidas1 = str(input(f"Escolha a sua primeira opção de chá predileta {armazena_lista}: ")).capitalize()
    opcao_bebidas2 = str(input(f"Escolha a sua segunda opção de chá predileta {armazena_lista}: ")).capitalize()
    opcao_bebidas3 = str(input(f"Escolha a sua terceira opção de chá predileta {armazena_lista}: ")).capitalize()
    
    armazena_resultado = [opcao_bebidas1, opcao_bebidas2, opcao_bebidas3]
    
    for bebida in armazena_resultado:
        if bebida in armazena_lista:
            print(f"Seus chás escolhidos foram: {bebida}")
        else:
            print(f"Está opção {bebida}, não é válida")

escolhaBebidas()
    #if  armazena_lista == opcao_bebidas:
     #   armazena_resultado = opcao_bebidas
      #  return f"Seus chás favoritos são: {armazena_resultado}"
    #else:
     #   return 'Está opção não é válida'
    
#print(escolhaBebidas())
