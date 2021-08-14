from datetime import date
ano = int(input('Escreva o seu ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('Voce tem {} anos e é da categoria MIRIM'.format(idade))
elif 14 >= idade > 9:
    print('Voce tem {} anos e é da categoria INFANTIL'.format(idade))
elif 19 >= idade > 14:
    print('Voce tem {} anos e é da categoria JUNIOR'.format(idade))
elif 25 >= idade > 19:
    print('Voce tem {} anos e é da categoria SENIOR'.format(idade))
else:
    print('Voce tem {} anos e é da categoria MASTER'.format(idade))
