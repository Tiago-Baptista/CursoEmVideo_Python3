from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
for k, v in jogo.items():
    print(f'{k} tirou {v}.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('=' * 30)
print('--------- RESULTADOS ---------')
print('=' * 30)
for i, v in enumerate(ranking):
    print(f'Em {i+1}º lugar ficou {v[0]} com {v[1]} pontos. ')
