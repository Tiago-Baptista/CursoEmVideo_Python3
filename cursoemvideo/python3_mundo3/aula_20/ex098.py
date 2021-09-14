from time import sleep
def contador(a, b, c):
    for t in range(a, b, c):
        sleep(0.5)
        print(f'{t} ', end='')
    sleep(2)
    print()


# Programa principal
print('Contagem de 1 a 10 de 1 em 1')
contador(1, 11, 1)
print('Contagem de 10 a 0 de 2 em 2')
contador(10, -1, -2)
print('Contagem personalizada')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if fim < 0:
    if inicio > fim:
        passo = -passo
        contador(inicio, fim - 1, passo)
    else:
        contador(inicio, fim - 1, passo)
else:
    if inicio > fim:
        passo = -passo
        contador(inicio, fim + 1, passo)
    else:
        contador(inicio, fim + 1, passo)
