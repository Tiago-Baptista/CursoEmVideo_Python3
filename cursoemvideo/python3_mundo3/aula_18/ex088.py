from random import randint
from time import sleep
mega = []
jogos = []
q = int(input('Quantos jogos quer sortear? '))
t = 1
while t <= q:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in mega:
            mega.append(n)
            cont += 1
        if cont >= 6:
            break
    mega.sort()
    jogos.append(mega[:])
    mega.clear()
    t += 1
for i, l in enumerate(jogos):
    print('Loading...')
    sleep(1)
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)
