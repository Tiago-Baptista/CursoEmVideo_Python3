nomes = ('Vanda', 'Monica', 'Tiago', 'Andre')
for n in nomes:
    print(f'\nNo nome {n.upper()} existem', end=' ')
    for vogal in n:
        if vogal.lower() in 'aeiou':
            print(vogal.lower(), end=' ')
