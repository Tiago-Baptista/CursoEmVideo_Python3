pessoas = list()
pessoa = dict()
total = 0
# Inserir registos
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Opação inválida. Escolha M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    total += pessoa['idade']
    pessoas.append(pessoa.copy())
    while True:
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if cont not in 'SN':
            print('Opação inválida. Escolha S ou N.')
        else:
            break
    if cont == 'N':
        break
print('=' * 30)
# Analise de dados
print(f'A) Foram registadas {len(pessoas)} pessoas.')
print(f'B) A média de idades foi de {total / len(pessoas)} anos.')
print(f'C) As mulheres registadas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) As pessoas com idade a cima da média são: ', end='')
for p in pessoas:
    if p['idade'] > (total / len(pessoas)):
        print(f'{p["nome"]} com {p["idade"]} anos ', end='')
print()
print('»»»»» FIM «««««')
