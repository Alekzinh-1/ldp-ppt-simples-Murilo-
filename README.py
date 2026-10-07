import random
pontuacao_player = 0
pontuacao_computador = 0
rodadas = 0
empates = 0
lista = []

print("Bem vindo ao Torneio de Jokenpo!\n Vence quem ganhar 3 vezes!")
while True:
   opcao_computador = random.randint(1, 3) 
   match opcao_computador:
       case 3:
           opcao_computador = "tesoura"
           fraqueza_computador = "pedra"
 
       case 2:
           opcao_computador = "papel"
           fraqueza_computador = "tesoura"
      
       case 1:
           opcao_computador = "pedra"
           fraqueza_computador = "papel"
           
           
 
   opcao_player = input("Pedra, Papel ou Tesoura?\n(ou deseja 'sair'?)").lower

   match opcao_player:
       case "tesoura":
           fraqueza_player = "pedra"
 
       case "papel":
           fraqueza_player = "tesoura"
      
       case "pedra":
           fraqueza_player = "papel"
        
       case "sair":
            print("Obrigado por jogar!")
            break
        
       case _:
           print("Insira uma opção válida.")
           continue
           
   if fraqueza_computador == opcao_player:
       print(f"{opcao_player} vence {opcao_computador}!")
       print("Vitória do Player!")
       lista.append(f"Computador: {opcao_computador}\n Player: {opcao_player}\n Resultado: Vitória Player!")
       pontuacao_player += 1
   
   elif fraqueza_player == opcao_computador:
       print(f"{opcao_computador} vence {opcao_player}!")
       print("Vitória do Computador!")
       lista.append(f"Computador: {opcao_computador}\n Player: {opcao_player}\n Resultado: Vitória Computador!")

       pontuacao_computador += 1
       
   else:
       print("Empate!\nJogada igual do Player e do Computador!")
       empates += 1
       

   print(f"Placar:\n Player: {pontuacao_player}\n Computador: {pontuacao_computador}")
   rodadas += 1

print(f""" 
      Total de rodadas: {rodadas}
      Empates: {empates}
      Lista: \n{lista}
      """)
pergunta = input("Deseja jogar novamente?(Y/N)").lower