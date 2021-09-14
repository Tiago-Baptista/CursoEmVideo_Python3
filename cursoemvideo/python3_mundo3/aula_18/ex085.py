lista = [[], []]
for c in range(1, 8):
    n = int(input(f'Escreva o {c}º numero: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print('=' * 70)
print(f'Os valores pares foram {sorted(lista[0])} \nOs valores impares foram {sorted(lista[1])}')
