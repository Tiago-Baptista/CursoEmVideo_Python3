def dobro(n=0, format=False):
    return n * 2 if not format else moeda(n * 2)


def metade(n=0, format=False):
    return n / 2 if not format else moeda(n / 2)    #Esta linha (not format)


def aumentar(n=0, p=0, format=False):
    r = n * (p / 100)
    return n + r if format is False else moeda(n + r)  #Igual a esta (format is False)


def diminuir(n=0, p=0, format=False):
    r = n * (p / 100)
    return n - r if format is False else moeda(n - r)


def moeda(n=0, moeda='€'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n=0, p=0):
    import moeda
    print('=' * 40)
    print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}'.center(40))
    print(f'Metade de {moeda.moeda(n)} é {moeda.metade(n, True)}'.center(40))
    print('-' * 40)
    print(f'Com {p}% de aumento fica em {moeda.aumentar(n, p, True)}'.center(40))
    print(f'Com {p}% de desconto fica em {moeda.diminuir(n, p, True)}'.center(40))
    print('=' * 40)
