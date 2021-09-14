liga = ('Sporting', 'Porto', 'Benfica', 'Braga', 'P.Ferreira', 'Guimarães',
        'S.Clara', 'Moreirense', 'Tondela', 'Portimonense', 'BSad', 'Maritimo',
        'Gil Vicente', 'Famalicão', 'Rio Ave', 'Boavista', 'Farense', 'Nacional')
print(f'--> Ordem de classificação: {liga}')
print(f'--> Os 5 primeiros classificados são: {liga[:5]}')
print(f'--> Os ultimos 4 classificados são: {liga[-4:]}')
print(f'--> Clubes por oredem alfabetica: {sorted(liga)}')
print('--> O Guimarães esta na {}ª posição'.format(liga.index('Guimarães') + 1))
