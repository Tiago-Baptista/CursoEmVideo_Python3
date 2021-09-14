# Interective help
'''help()
help(print)
print(input.__doc__)'''

#Docstring
'''def contador(i, f, p):
    """
    Faz uma contagem e mostra no ecrã
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='.. ')
        c += p
    print('FIM!')


contador(2, 10, 2)
help(contador)'''

#Parametros Opcionais
'''def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma dá {s}')


somar(3, 2, 5)
somar(8, 4)
somar()'''

#Escopo de variaveis
'''def teste():
    #global n
    n = 3
    x = 8
    print(f'Na função teste, n vale {n}') #escopo local
    print(f'Na função teste, x vale {x}')
n = 2
teste()
print(f'No programa principal, n vale {n}') #escopo global'''

#Retorno de valores
'''def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Os meus calculos deram {r1}, {r2} e {r3}.')'''


#Exercicio pratico
def factorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um numero: '))
print(f'O factorial de {n} é igual a {factorial(n)}')
