temp = list()
lista = list()
peso = []
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    peso.append(temp[1])
    lista.append(temp[:])
    temp.clear()
    c = str(input('Quer continuar [S/N]? ')).strip().lower()[0]
    if c == 'n':
        break
print(f'Voce inseriu {len(lista)} pessoas.')
print(f'O maior peso foi de {max(peso):.2f}Kg. Peso de ', end='')
for p in lista:
    if p[1] == max(peso):
        print(f'{p[0]}')
print(f'O menor peso foi de {min(peso):.2f}Kg. Peso de ', end='')
for p in lista:
    if p[1] == min(peso):
        print(f'{p[0]}')
