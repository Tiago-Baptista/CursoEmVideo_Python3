sexo = str(input('Qual o seu sexo? [M/F] ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Escreva uma opção válida: ')).upper().strip()[0]
print('Sexo {} registado com sucesso!'.format(sexo))
