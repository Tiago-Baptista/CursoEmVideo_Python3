'''for c in range(1, 10):
    print(c)                   #este
print('FIM')'''

'''c = 1
while c < 10:
    print(c)               #igual a este
    c = c + 1
print('FIM')'''

'''n = 1
while n != 0:
    n = int(input('Escreva um numero: '))
print('FIM')'''

'''r = 'S'
while r == 'S':
    n = int(input('Escreva um numero: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('FIM')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Escreveu {} numeros pares e {} numeros impares.'.format(par, impar))
