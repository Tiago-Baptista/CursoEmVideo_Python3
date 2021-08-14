n1 = int(input('Escreva um numero inteiro: '))
n2 = int(input('Escreva outro numero inteiro: '))
if n1 > n2:
    print('Comparando o {} e o {} o numero {} é o maior'.format(n1, n2, n1))
elif n2 > n1:
    print('Comparando o {} e o {} o numero {} é o maior'.format(n1, n2, n2))
else:
    print('Comparando o {} e o {}, eles são iguais'.format(n1, n2))
