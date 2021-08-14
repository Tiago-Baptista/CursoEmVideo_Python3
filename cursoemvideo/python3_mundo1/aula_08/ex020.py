import random
a = input('Nome do primeiro aluno: ')
b = input('Nome do segundo aluno: ')
c = input('Nome do terceiro aluno: ')
d = input('Nome do quarto aluno: ')
x = [a, b, c, d]
random.shuffle(x)
print('A ordem de escolha é ')
print(x)
