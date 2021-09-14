lista = []
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    r = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if r == 'N':
        break
print('=-' * 30)
print(f'Foram digitados {len(lista)} numeros.')
lista.sort(reverse=True)
print(f'A lista por ordem decrescente é {lista}')
if 5 in lista:
    print(f'O numero 5 faz parte da lista!')
else:
    print('O numero 5 não faz parte da lista!')
