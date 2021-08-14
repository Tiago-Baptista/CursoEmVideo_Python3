import random
from time import sleep
print('Tente acertar no numero sorteado')
n = int(input('Escreva um numero inteiro de 0 a 5: '))
x = random.randint(0, 5)
print('Loading...')
sleep(3)
print('O numero sorteado é {}'.format(x))
if n == x:
    print('Você ganhou!')
else:
    print('Você perdeu!')
