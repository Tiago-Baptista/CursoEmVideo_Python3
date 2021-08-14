t = 0
n = int(input('Digite um numero: '))
for c in range(1, n+1):
    if n % c == 0:
        print('\033[31m', end='')
        t += 1
    else:
        print('\033[m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(n, t))
if t == 2:
    print('O seu numero é primo!')
else:
    print('O seu numero não é primo')
