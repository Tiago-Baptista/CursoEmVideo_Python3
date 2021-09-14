lista = []
for c in range(0, 5):
    n = int(input('Digite um numero: '))
    if c == 0:
        lista.append(n)
        print('Valor adicionado no inicio da lista')
    elif n > lista[-1]:
        lista.append(n)
        print('Valor adicionado no final da lista')
    else:
        p = 0
        while p < len(lista):
            if n <= lista[p]:
                lista.insert(p, n)
                print(f'Valor adicionado na posição {p}')
                break
            p += 1
print(f'Os vamolres digitados foram {lista}')
