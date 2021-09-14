from time import sleep
def maior(*num):
    cont = maior = 0
    print('Analizando os valores...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print()
    print(f'Foram informados {cont} valores')
    print(f'O maior valor foi {maior}')
    print('-' * 30)
    sleep(1)


# Programa Principal
maior(9, 5, 6, 7, 3, 4)
maior(2, 5, 7, 1)
maior(0, 5, 9, 7, 1, 6, 3, 4, 5)
maior()
