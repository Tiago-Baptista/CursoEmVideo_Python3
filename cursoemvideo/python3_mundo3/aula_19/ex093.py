dados = {}
golos = []
tot = 0    #desnecessario com o sum(golos)
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(1, partidas+1):
    g = int(input(f'Quantos golos no jogo {c}: '))
    golos.append(g)
    if g > 0:                  #desnecessario com o sum(golos)
       tot += g                #desnecessario com o sum(golos)
dados['golos'] = golos[:]
dados['totgolos'] = tot   #podia tambem ser da seguinte forma: dados['totgolos'] = sum(golos)
print('***' * 20)
print(f'O jogador {dados["nome"]} jogou {partidas} jogos.')
for k, v in enumerate(golos):
    print(f'No jogo {k+1} ele fez {v} golos.')
print(f'Marcou {tot} golos no total.')
