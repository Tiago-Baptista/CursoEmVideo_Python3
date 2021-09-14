lista = list()
while True:
    n = (int(input('Digite um valor: ')))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado. Não adicionado!')
    c = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if c == 'N':
        break
print(f'Voce adicionou os numeros {sorted(lista)}')
