jogadores = []
dados = {}
golos = []
# inserir registos
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    golos.clear()
    for c in range(1, partidas+1):
        g = int(input(f'Quantos golos no jogo {c}: '))
        golos.append(g)
    dados['golos'] = golos[:]
    dados['totgolos'] = sum(golos)
    jogadores.append(dados.copy())
    while True:
        cont = str(input('Registar outro jogador? [S/N] ')).strip().upper()[0]
        if cont not in 'SN':
            print(f'Erro! Escreva apenas S ou N.')
        if cont in 'SN':
            break
    if cont == 'N':
        break
print('***' * 20)
# Analisar dados
print('=' * 45)
print('Cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=' * 45)
while True:
    op = int(input('Mostrar as estatisticas do jogador No (999 termina): '))
    if op == 999:
        break
    if op >= len(jogadores):
        print(f'Jogador inexistente! Tente outro.')
    else:
        print(f'Estatisticas do jogador {jogadores[op]["nome"]}:')
        for k, v in enumerate(jogadores[op]["golos"]):
            print(f' -> No jogo {k+1} ele fez {v} golos.')
        print(f' -> Marcou {jogadores[op]["totgolos"]} golos no total.')
    print('***' * 20)
