print('\033[31mSequencia de Fibonacci!\033[m')
n = int(input('Quantos termos quer mostrar? '))
t1 = 0
t2 = 1
t3 = t1 + t2
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' --- Fim')
