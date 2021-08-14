print('»' * 25)
print('Digite 999 para terminar!')
print('«' * 25)
c = soma = 0
while True:
    n = int(input('Escreva um numero: '))
    if n == 999:
        break
    c += 1
    soma += n
print(f'Foram digitados \033[1;31m{c}\033[m numeros e a sua soma é \033[1;31m{soma}\033[m')
