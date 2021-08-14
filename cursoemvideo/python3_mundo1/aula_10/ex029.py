print('O limite de velocidade é de 80km/h')
velocidade = float(input('A sua velocidade é: km/h '))
if velocidade > 80:
    print('Voce está em excesso de velocidade {}km/h!\nA multa será de: {:.2f}€'.format((velocidade - 80), ((velocidade - 80) * 7)))
else:
    print('A sua velocidade é boa, {}km/h abaixo do limite premitido!'.format(velocidade - 80))
    print('Boa viagem!')
