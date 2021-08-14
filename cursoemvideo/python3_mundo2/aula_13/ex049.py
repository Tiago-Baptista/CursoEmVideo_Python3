n = int(input('Escreva um numero inteiro: '))
print('-' * 12)
for c in range(1, 11):
    t = n * c
    print('{} x {:2} = {}'.format(n, c, t))
print('-' * 12)
