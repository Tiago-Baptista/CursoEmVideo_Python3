total = mil = menor = c = 0
barato = ''
while True:
    produto = str(input('Produto: ')).strip().lower()
    preço = float(input('Preço: €'))
    cont = str(input('Continuar [S/N]? ')).strip().lower()[0]
    c += 1
    total += preço
    if preço >= 1000:
        mil += 1
    if c == 1:          # or preço < menor ---> elimina o else
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    while cont not in 'sn':
        cont = str(input('Continuar [S/N]? ')).strip().lower()[0]
    if cont == 'n':
        break
print('=' * 50)
print(f'O total da compra foi {total:.2f}€')
print(f'Voce comprou {mil} produtos com o preço superior a 1000€')
print(f'A compra de menor valor foi \033[1m\033[4m{produto}\033[m que custou {menor:.2f}€')
