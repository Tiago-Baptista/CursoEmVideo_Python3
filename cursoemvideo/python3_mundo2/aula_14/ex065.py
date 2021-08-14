stop = ''
soma = c = maior = menor = 0
while stop != 'N':
    n = int(input('Digite outro numero inteiro: '))
    stop = str(input('Quer outro numero [S/N]? ')).strip().upper()[0]
    if stop != 'S' and stop != 'N':
        print('\033[31mOpção inválida! Numero anterior desconsiderado.\033[m')
    else:
        soma += n
        c += 1
        media = soma / c
        if maior == 0:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
print('A média de todos os valores lidos é de {:.2f}'.format(media))
print('O maior numero foi {} e o menor foi {}.'.format(maior, menor))
