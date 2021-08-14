'''from math import factorial
print('=' * 40)
print('\033[31mVamos calcular o fatorial de um numero!\033[m')
print('=' * 40)
n = int(input('Escreva um numero: '))
f = factorial(n)
print('O factorial de {} é {}'.format(n, f))'''

print('=' * 40)
print('\033[31mVamos calcular o fatorial de um numero!\033[m')
print('=' * 40)
n = int(input('Escreva um numero: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
