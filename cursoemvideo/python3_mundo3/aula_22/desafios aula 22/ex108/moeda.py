def dobro(n=0):
    return n * 2


def metade(n=0):
    return n / 2


def aumentar(n=0, p=0):
    r = n * (p / 100)
    return n + r


def diminuir(n=0, p=0):
    r = n * (p / 100)
    return n - r


def moeda(n=0, moeda='€'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
