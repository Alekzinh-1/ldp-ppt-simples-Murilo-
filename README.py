import random
print("Bem vindo ao Torneio de Jokenpo!\nVence quem ganhar 3 vezes!")

while True:
    pontuacao_player = 0
    pontuacao_computador = 0
    rodadas = 0
    empates = 0
    jogadas_computador = [] 
    jogadas_player = []
    resultado = []
    rounds = []
    while pontuacao_player < 3 and pontuacao_computador < 3:
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
           
        print("==" * 10)        
        print(f"Rodada {rodadas + 1}!")
        print("==" * 10)
        opcao_player = input("Pedra, Papel ou Tesoura? (ou 'sair' para encerrar o jogo)\n").lower()

        if opcao_player == "tesoura":
            fraqueza_player = "pedra"
 
        elif opcao_player == "papel":
            fraqueza_player = "tesoura"
      
        elif opcao_player == "pedra":
            fraqueza_player = "papel"
        
        elif opcao_player == "sair":
             print("Obrigado por jogar!")
             break
        
        else:
            print("Insira uma opção válida.")
            continue
   
        print("==" * 10)
        if fraqueza_computador == opcao_player:
            print(f"{opcao_player} vence {opcao_computador}!")
            print("------- VITÓRIA! -------")
            jogadas_player.append(opcao_player)
            jogadas_computador.append(opcao_computador)
            resultado.append("Vitória Player!")
            pontuacao_player += 1
   
        elif fraqueza_player == opcao_computador:
            print(f"{opcao_computador} vence {opcao_player}!")
            print("------- DERROTA! -------")
            jogadas_computador.append(opcao_computador)
            jogadas_player.append(opcao_player)
            resultado.append("Vitória Computador!")
            pontuacao_computador += 1

        else:
            print("------- EMPATE! -------")
            print("Jogadas iguais Player e Computador!")
            jogadas_computador.append(opcao_computador)
            jogadas_player.append(opcao_player)
            resultado.append("Empate!")
            empates += 1

        print(f"Placar:\n Player: {pontuacao_player} | Computador: {pontuacao_computador}")
        rodadas += 1
        rounds.append(rodadas)

    print("==" * 10)
    if pontuacao_player == 3:
        print("""
              Meus parabéns! 
              Você venceu o torneio!
              """)
    elif pontuacao_computador == 3:
        print(""" 
              O computador venceu o torneio! 
              Tente novamente ou desista!
             """)
    
    print("==" * 10)
    print(f""" 
Total de rodadas: {rodadas}
Empates: {empates}
      """)        
    print("Placar final:")
    for i in range(rodadas):
        print(f"{rounds[i]}°: {jogadas_player[i]}  vs  {jogadas_computador[i]} | {resultado[i]}")
    
    pergunta = input("Deseja jogar novamente?(Y/N)\n").lower()
    if pergunta == "y":
        print("Reiniciando o jogo...")
        continue
    else:
        print("Obrigado por jogar!")
        break
