import random
from time import sleep
n = 1
soma = 1
x = random.randint(0, 10)
print('-=' * 16)
print('Tente acertar no numero sorteado')
print('-=' * 16)
while n != x:
    n = int(input('Escreva um numero inteiro de 0 a 10: '))
    print('Loading...')
    sleep(2)
    if n == x:
        print('\033[1;33mVocê ganhou!\033[m')
    else:
        soma += 1
        if n < x:
            print('\033[1;31mVocê perdeu!\033[m Tente um numero maior...')
        elif n > x:
            print('\033[1;31mVocê perdeu!\033[m Tente um numero menor...')
print('Voce precisou de \033[1;36m{}\033[m tentativas para ganhar!'.format(soma))
