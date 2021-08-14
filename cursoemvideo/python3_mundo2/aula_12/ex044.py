print('{:=^40}'.format(' LOJAS BAPTISTA '))
preço = float(input('Qual o valor do produto? €'))
print('''Escolha uma forma de pagamento
[ 1 ] Compra á vista em dinheiro
[ 2 ] Compra á vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Sua opção: '))
desconto1 = preço - (preço * 10 / 100)
desconto2 = preço - (preço * 5 / 100)
juros = preço + (preço * 20 / 100)
if opção == 1:
    print('Terá 10% de desconto e o preço final será de {:.2f}€'.format(desconto1))
elif opção == 2:
    print('Terá 5% de desconto e o preço final será de {:.2f}€'.format(desconto2))
elif opção == 3:
    print('O preço será o normal, paragá {:.2f}€'.format(preço))
elif opção == 4:
    print('Ao preço acresce 20% de juros e o preço final será de {:.2f}€'.format(juros))
else:
    print('Opção de pagamento inválida. Escolha uma opção válida!')
