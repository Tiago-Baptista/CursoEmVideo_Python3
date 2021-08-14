print('=' * 33)
print('OS 10 PRIMEIROS TERMOS DE UMA PA!')
print('=' * 33)
n = int(input('Escreva o primeiro termo: '))
r = int(input('Escreva a razão: '))
termo = n
cont = 1
while cont <= 10:
    print('{} '.format(termo), end= '> ')
    termo += r
    cont += 1
print('Acabou!')
