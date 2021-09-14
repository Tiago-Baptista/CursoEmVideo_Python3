from datetime import datetime
t = dict()
t['nome'] = str(input('Nome: ')).capitalize()
nascimento = int(input('Nascimento: '))
t['idade'] = datetime.now().year - nascimento
t['cpts'] = int(input('Carteira de trabalho (0 se não tem): '))
if t['cpts'] != 0:
    t['anocrt'] = int(input('Ano de contratação: '))
    t['salario'] = float(input('Salário: €'))
    t['aposen'] = t['idade'] + ((t['anocrt'] + 40) - datetime.now().year)
print('***' * 20)
for k, v in t.items():
    print(f'{k}: {v}')
