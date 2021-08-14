from math import hypot
cat1 = float(input('Comprimento do cateto oposto: '))
cat2 = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa é igual a {:.2f}'.format(hypot(cat1, cat2)))
