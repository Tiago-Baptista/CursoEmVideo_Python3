'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


# Programa Principal
soma(b=4, a=5)
soma(2, 1)'''


def contador(*num):
    for valor in num:
        print(f'{valor}', end='')
    print()
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros.')


contador(0, 8)
contador(2, 5, 8, 3)
contador(9, 5, 8, 6, 3, 0)


'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [2, 4, 6, 8]
dobra(valores)
print(valores)'''
