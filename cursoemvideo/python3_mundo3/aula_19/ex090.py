sit = {}
sit['nome'] = str(input('Nome: '))
sit['media'] = float(input('Media: '))
print('=-=' * 20)
print(f'O nome do aluno é {sit["nome"]}')
print(f'A sua média é de {sit["media"]}')
if sit['media'] >= 10:
    sit['resultado'] = 'Aprovado'
    print(f'O aluno foi \033[1;32m{sit["resultado"]}\033[m')
else:
    sit['resultado'] = 'Reprovado'
    print(f'O aluno foi \033[1;31m{sit["resultado"]}\033[m')
