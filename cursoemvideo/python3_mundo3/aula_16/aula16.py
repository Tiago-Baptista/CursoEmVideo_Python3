'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')   #tuplas são imutáveis
print(lanche[1:3])
print(lanche[:2])
print(lanche[-3:])'''

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for c in lanche:
    print(f'Eu vou comer {c}')
print('Comi bue!!!')

for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posição {c}')
print('Comi bue!!!')

for p, c in enumerate(lanche):
    print(f'Eu vou comer {c} na posição {p}')
print('Comi bue!!!')

print(sorted(lanche))
print(lanche)

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
print(a)
print(b)
c = a + b
print(c)
print(len(c))
print(c.count(5))
print(c.index(8)) #posição'''

'''pessoa = ('Tiago', 40, 'M', 103)
#del(pessoa)  apagar tupla
print(pessoa)'''
