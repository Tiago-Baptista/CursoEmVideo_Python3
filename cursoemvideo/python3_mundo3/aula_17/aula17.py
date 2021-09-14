'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0) #posição e numero a inserir
num.pop(0) #elimina a posição. sem nada elimina o ultimo
if 4 in num:
    num.remove(4) # remove o elemento e não a posição
else:
    print('Não achei o numero 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')'''

'''a = [2, 3, 4, 7]
# b = a  #b fica ligado a a
b = a[:] #copia os valores mas não fica ligado a a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''

valores = list()
'''valores.append(5)
valores.append(9)
valores.append(4)'''
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} eu encontrei o valor {v}!')
print(valores)