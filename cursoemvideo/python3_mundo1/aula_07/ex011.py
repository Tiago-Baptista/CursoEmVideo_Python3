largura = float(input('Largura da parede em metros: '))
altura = float(input('Altura da parede em metros: '))
area = largura * altura
print('Litros de tinta necessário para pintar a parede: {:.2f}L'.format(area / 2))
