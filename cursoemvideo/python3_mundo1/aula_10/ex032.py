import datetime
ano = int(input('Escreva um ano e veja se ele é bissexto: '))
if ano == 0:
    ano = datetime.date.today().year    # coloque 0 para saber o ano atual
bi = ano % 4 and ano % 100 != 0 or ano % 400 == 0
if bi == 0:
    print('Esse ano {} é bissexto!'.format(ano))
else:
    print('Esse ano {} não é bissexto!'.format(ano))
