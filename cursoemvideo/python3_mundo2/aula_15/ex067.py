while True:
    n = int(input('Escreva um numero para saber a sua tabuada: '))
    if n < 0:
        break
    for c in range(0, 10):
        c += 1
        tabuada = n * c
        print(f'{n} X {c} = {tabuada}')
print('\033[31mPrograma terminado!')
