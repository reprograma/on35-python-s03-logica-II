#Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, pergunte quantos e mostre na tela uma mensagem de sua escolha. No caso de o usuário responder “não”, pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.

tem_irmaos = input("Você tem irmãos? (sim/não): ")

if tem_irmaos.lower() == "sim":
  numero_irmaos = int(input("Quantos irmãos você tem? "))
  if numero_irmaos > 1:
    print(f"Que legal ter {numero_irmaos} irmãos! Vocês devem se divertir muito juntos.")
  else:
    print("Ter um irmão ou irmã pode ser muito especial. Você tem uma ótima companhia!")
else:
  gostaria_irmaos = input("Você gostaria de ter irmãos? (sim/não): ")
  if gostaria_irmaos.lower() == "sim":
    print("Ter irmãos pode trazer muitas alegrias e aprendizados. Você com certeza faria ótimas amizades!")
  else:
    print("Tudo bem, não ter irmãos também tem suas vantagens. Você pode ter mais privacidade e tempo para si mesmo.")


