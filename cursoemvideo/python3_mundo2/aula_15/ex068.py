from random import randint
from time import sleep
print('=-' * 14)
print('Vamos jogar par ou impar!!!')
print('-=' * 14)
c = 0
while True:
    escolha = str(input('Par ou impar? ')).strip().lower()[0]
    jogador = int(input('Sua jogada (numero de 0 a 10): '))
    computador = randint(0, 10)
    sleep(1)
    print(f'Jodada PySábio: \033[32m{computador}\033[m')
    resultado = jogador + computador
    print(f'O resultado é \033[1m\033[4m{resultado}\033[m')
    p = resultado % 2 == 0
    i = resultado % 2 == 1
    if escolha == 'p' and p == True:
        print('\033[33mVoce ganhou!\033[m')
        c += 1
    elif escolha == 'i' and i == True:
        print('\033[33mVoce ganhou!\033[m')
        c += 1
    else:
        print('\033[34mVoce perdeu!\033[m')
        break
    print('=-' * 20)
print('=-' * 20)
print(f'Voce ganhou \033[31m{c}\033[m vezes!')
print('=-' * 20)
