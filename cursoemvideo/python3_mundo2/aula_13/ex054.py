from datetime import date
cont = 0
cont2 = 0
for c in range(0, 7):
    ano = int(input('Seu ano de nascimento: '))
    idade = date.today().year - ano
    if idade >= 18:
        cont += 1
    else:
        cont2 += 1
print('\033[31m{}\033[m pessoas são maiores de idade e '.format(cont), end='')
print('\033[31m{}\033[m são menores de idade.'.format(cont2))
