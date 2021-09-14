import moeda
n = float(input('Digite o preço: €'))
p = int(input('Digite uma porcentagem: %'))
print(f'O dobro de {n} é {moeda.dobro(n)}')
print(f'Metade de {n} é {moeda.metade(n)}')
print(f'O preço com {p}% de aumento fica em {moeda.aumentar(n, p)}')
print(f'O preço com {p}% de desconto fica em {moeda.diminuir(n, p)}')
