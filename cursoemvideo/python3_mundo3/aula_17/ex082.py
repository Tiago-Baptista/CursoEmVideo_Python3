lista1 = list()
lista2 = []
lista3 = []
while True:
    n = int(input('Digite um numero: '))
    r = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    lista1.append(n)
    if n % 2 == 0:
        lista2.append(n)
    if n % 2 == 1:
        lista3.append(n)
    if r == 'N':
        break
print(f'Os valores digitados foram: {sorted(lista1)}')
print(f'Os numeros pares foram: {sorted(lista2)}')
print(f'Os numeros impares foram: {sorted(lista3)}')
