lista1 = []
lista2 = []
ex = str(input('Escreva uma expressão matemática e verifique se ela é válida: '))
for s in ex:
    if s == '(':
        lista1.append(s)
    if s == ')':
        lista2.append(s)
if len(lista1) == len(lista2):
    print('A sua função é válida!')
else:
    print('A sua função não é válida!')
