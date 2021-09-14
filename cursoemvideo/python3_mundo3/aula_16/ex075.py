n1 = int(input('Escreva um numero: '))
n2 = int(input('Escreva outro numero: '))
n3 = int(input('Escreva mais um numero: '))
n4 = int(input('Escreva o ultimo numero: '))
t = (n1, n2, n3, n4)
print(f'Escreveu os numeros {t}')
print(f'O numero 9 foi escrito {t.count(9)} vezes')
if 3 in t:
    print(f'O primeiro numero 3 vem na posição {t.index(3)+1}')
else:
    print(f'O numero 3 não está em nenhuma posição')
print(f'Os numeros pares foram: ', end='')
for n in t:
    if n % 2 == 0:
        print(n, end=' ')
