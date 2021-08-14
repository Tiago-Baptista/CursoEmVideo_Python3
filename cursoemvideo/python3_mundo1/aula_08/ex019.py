from random import choice
a = input('Nome do primeiro aluno: ')
b = input('Nome do segundo aluno: ')
c = input('Nome do terceiro aluno: ')
d = input('Nome do quarto aluno: ')
x = [a, b, c, d]
print('De entre os alunos {}, {}, {} e {}, quem vai apagar o quadro é o {}'.format(a, b, c, d, choice(x)))
