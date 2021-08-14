print('=' * 50)
print('{:^50}'.format('BANCO TB'))
print('=' * 50)
lev = int(input('Valor a levantar: €'))
total = lev
nota = 50
totalnota = 0
while True:
    if total >= nota:
        total -= nota
        totalnota += 1
    else:
        if totalnota != 0:
            print(f'Total de {totalnota} notas de {nota}€')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        totalnota = 0
        if total == 0:
            break
