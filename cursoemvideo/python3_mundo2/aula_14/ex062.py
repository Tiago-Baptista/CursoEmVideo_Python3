print('=' * 33)
print('OS 10 PRIMEIROS TERMOS DE UMA PA!')
print('=' * 33)
n = int(input('Escreva o primeiro termo: '))
r = int(input('Escreva a razão: '))
termo = n
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} '.format(termo), end='> ')
        termo += r
        cont += 1
    print('Pausa')
    mais = int(input('Quer mostrar mais alguns termos? Quantos? '))
print('A progressão foi terminada com {} termos mostrados.'.format(total))
