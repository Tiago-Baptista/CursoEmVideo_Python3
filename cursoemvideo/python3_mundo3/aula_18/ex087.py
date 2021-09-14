matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sl = []
par = sc = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um numero para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            par += matriz[linha][coluna]
        if coluna == 2:
            sc += matriz[linha][coluna]
        if linha == 1:
            sl.append(matriz[linha][coluna])
print('=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('=' * 30)
print(f'A soma de todos os numeros pares é {par}')
print(f'A soma dos numeros da 3ª coluna é {sc}')
print(f'O maior numero da 2ª linha é {max(sl)}')
