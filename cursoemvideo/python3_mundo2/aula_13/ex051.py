print('=' * 33)
print('OS 10 PRIMEIROS TERMOS DE UMA PA!')
print('=' * 33)
n = int(input('Escreva o primeiro termo: '))
r = int(input('Escreva a razão: '))
dec = n + (10-1) * r
for c in range(n, dec + r, r):
    print('{} '.format(c), end= '> ')
print('Acabou!')
