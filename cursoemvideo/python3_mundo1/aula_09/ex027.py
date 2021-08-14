nome = str(input('Escreva o seu nome: ')).strip()
x = nome.split()
print('O seu primeiro nome é {}'.format(x[0]))
print('O seu ultimo nome é {}'.format(x[len(x)-1]))
