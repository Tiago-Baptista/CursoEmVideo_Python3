from datetime import date
ano = int(input('Qual é o seu ano de nascimento? '))
idade = date.today().year - ano
if idade == 18:
    print('Voce tem {} anos e está na hora de se alistar para o exercito!'.format(idade))
elif idade < 18:
    print('Voce tem {} anos, ainda é cedo para se alistar. Faltam {} anos!'.format(idade, (18-idade)))
else:
    print('Voce tem {} anos e já passou da idade de se alistar! Passaram {} anos.'.format(idade, (idade-18)))
