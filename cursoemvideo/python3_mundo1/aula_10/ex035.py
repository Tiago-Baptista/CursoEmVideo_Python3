r1 = float(input('Escreva a medida de uma recta em cm: '))
r2 = float(input('Escreva a medida de outra recta em cm: '))
r3 = float(input('Escreva a medida de outra recta em cm: '))
if (r2 + r3) > r1 and (r1 + r3) > r2 and (r1 + r2) > r3:
    print('As suas rectas conseguem fazer um triangulo')
else:
    print('As suas rectas não conseguem formar um triangulo')
