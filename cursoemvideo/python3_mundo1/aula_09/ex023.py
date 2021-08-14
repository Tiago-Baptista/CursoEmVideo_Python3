numero = int(input('Escreva um numero de 0 a 9999: '))
m = numero // 1000 % 10
c = numero // 100 % 10
d = numero // 10 % 10
u = numero // 1 % 10
print('O algarismo dos milhares é {}'.format(m))
print('O algarismo das centenas é {}'.format(c))
print('O algarismo das dezenas é {}'.format(d))
print('O algarismo das unidades é {}'.format(u))
