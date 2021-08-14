km = float(input('Km percorridos: '))
dias = int(input('Dias alugados: '))
p = (km * 0.15) + (dias * 60)
print('O preço a pagar é: {:.2f}€'.format(p))
