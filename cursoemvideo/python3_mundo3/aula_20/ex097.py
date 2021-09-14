def escreva(msg):
    print('~' * len(a) + '~~~~~~')
    print(f'   {a}   ')    #3 espaços de cada lado
    print('~' * len(a) + '~~~~~~')


#Programa principal
a = str(input('Escreva uma palavra para sair formatada: ')).strip()
escreva(a)
