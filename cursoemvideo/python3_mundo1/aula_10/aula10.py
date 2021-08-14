#nome = str(input('Qual é o seu nome: '))
#if nome == 'Gustavo':
#    print('Que nome lindo!')
#print('Bom dia {}!'.format(nome))


#nome = str(input('Qual é o seu nome: '))
#if nome == 'Gustavo':
 #   print('Que nome lindo!')
#else:
 #   print('Que nome tão normal...')
#print('Bom dia {}!'.format(nome))


n1 = float(input('Escreva a primeira nota: '))
n2 = float(input('Escreva a segunda nota: '))
m = (n1 + n2)/2
print('A tua média é: {:.2f}'.format(m))
print('Parabens!' if m >= 6 else 'Estude mais!')
