distancia = float(input('Distancia precorrida em km: '))
if distancia > 200:
    x = distancia * 0.45
    print('O preço a apagar é de: {:.2f}€'.format(x))
else:
    y = distancia * 0.50
    print('O preço a pagar é de: {:.2f}€'.format(y))
