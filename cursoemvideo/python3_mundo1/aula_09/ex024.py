cidade = str(input('escreva o nome de uma cidade: ')).strip()
x = cidade[:5].upper() == 'SANTO'
print('A cidade contem o nome Santo? {}'.format(x))
