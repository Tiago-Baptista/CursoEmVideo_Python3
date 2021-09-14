valores = list()
for v in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print('=' * 50)
print(f'Os valores inseridos foram {valores}')
print(f'O maior valor foi {max(valores)} e está na posição ', end='')
for p, i in enumerate(valores):
    if i == max(valores):
        print(f'{p}...', end='')
print()
print(f'O menor valor foi {min(valores)} e está na posição ', end='')
for p, i in enumerate(valores):
    if i == min(valores):
        print(f'{p}...', end='')
print()
