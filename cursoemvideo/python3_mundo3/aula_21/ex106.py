c = ('\033[m',       # 0 sem cor
     '\033[1;31m',   # 1 vermelho
     '\033[1;32m',   # 2 verde
     '\033[1;33m',   # 3 amarelo
     '\033[1;34m',   # 4 azul
     '\033[1;35m',   # 5 roxo
     )


def ajuda(com):
    titulo(f'Acedendo ao manual do comando {com}', 4)
    print(c[3], end='')
    help(com)
    print(c[0], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 6
    print(c[cor], end='')
    print('*' * tam)
    print(f'   {msg}')
    print('*' * tam)
    print(c[0], end='')


#Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 1)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('VOLTE SEMPRE!', 5)
