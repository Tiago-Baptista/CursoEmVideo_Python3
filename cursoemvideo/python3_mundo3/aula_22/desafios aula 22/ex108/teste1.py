import moeda
n = float(input('Digite o preço: €'))
p = int(input('Digite uma porcentagem: %'))
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'Metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')
print(f'O preço com {p}% de aumento fica em {moeda.moeda(moeda.aumentar(n, p))}')
print(f'O preço com {p}% de desconto fica em {moeda.moeda(moeda.diminuir(n, p))}')
