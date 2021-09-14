lista = ('Pão', 3.15, 'Arroz', 1.09, 'Cerveja', 1.49,
         'Farinha', 0.89, 'Café', 2.99, 'Caraguejo Real', 103,
         'Champanhe', 25.75)
print('-' * 50)
print(f'{"LISTA DE PREÇOS":^50}')
print('-' * 50)
for p in range(0, len(lista)):
    if p % 2 == 0:
        print(f'{lista[p]:.<40}', end='')
    else:
        print(f'{lista[p]:>8.2f}€')
print('-' * 50)
