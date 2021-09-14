aluno = []
alunos = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    cont = str(input('Quer continuar [S/N]: ')).strip().lower()[0]
    aluno.append(nome)
    aluno.append(n1)
    aluno.append(n2)
    aluno.append(media)
    alunos.append(aluno[:])
    aluno.clear()
    if cont == 'n':
        break
print('=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')
print('=' * 30)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[3]:>8.1f}')
print('=' * 30)
while True:
    op = int(input('Mostrar as notas do aluno No (999 termina): '))
    if op == 999:
        break
    if op <= len(alunos) - 1:
        print(f'As notas de {alunos[op][0]} foram {alunos[op][1]} e {alunos[op][2]}')
