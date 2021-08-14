sexo = ''
maior = macho = menor = 0
while True:
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Qual o seu sexo [M/F]? ')).strip().lower()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'm':
        macho += 1
    if sexo == 'f' and idade < 20:
        menor += 1
    while sexo not in 'mf':
        sexo = str(input('Qual o seu sexo [M/F]? ')).strip().lower()[0]
    print('\033[31mResisto inserido com sucesso!\033[m')
    cont = str(input('Quer continuar a resistar [S/N]? ')).strip().lower()[0]
    while cont not in 'sn':
        cont = str(input('Quer continuar a resistar [S/N]? ')).strip().lower()[0]
    if cont == 'n':
        break
print('=' * 50)
print(f'Foram resistadas {maior} pessoas maiores de 18 anos.')
print(f'Foram resistados {macho} homens.')
print(f'Foram resistadas {menor} mulheres com menos de 20 anos.')
