nome = str(input('QUal é o seu nome? '))
if nome == 'Tiago' or nome == 'Diogo' or nome == 'Carolina':
    print('Que nome bonito!')
elif nome == 'José' or nome == 'Maria':
    print('O seu nome é bem popular em Portugal!')
elif nome in 'Ana Tania Rute':
    print('Nome feminino bem bonito!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
