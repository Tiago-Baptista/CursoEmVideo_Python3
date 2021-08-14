casa = float(input('Qual o valor do imovel? €'))
salario = float(input('Qual o seu ordenado? €'))
anos = int(input('Em quantos anos vai pagar? '))
prestação = casa / (anos * 12)
if prestação <= (salario * 30 / 100):
    print('O seu credito foi aprovado!')
    print('A sua prestação é de {:.2f}€'.format(prestação))
else:
    print('O seu credito foi reprovado. Lamentamos!')
