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
