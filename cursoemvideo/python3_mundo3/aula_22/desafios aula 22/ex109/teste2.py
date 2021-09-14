import moeda
n = float(input('Digite o preço: €'))
p = int(input('Digite uma porcentagem: %'))
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}')
print(f'Metade de {moeda.moeda(n)} é {moeda.metade(n, True)}')
print(f'O preço com {p}% de aumento fica em {moeda.aumentar(n, p, True)}')
print(f'O preço com {p}% de desconto fica em {moeda.diminuir(n, p, True)}')
