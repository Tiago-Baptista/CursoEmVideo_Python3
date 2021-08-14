soma = 0
ma = 0
fe = 0
x = 0
maior = 0
velho = ''
for c in range(1, 5):
    nome = str(input('Escreva o seu nome: ')).strip().upper()
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Qual o seu sexo [M/F]? ')).strip().lower()
    soma += idade
    media = soma / 4
    if sexo == 'f' and idade < 20:
        x += 1
    if c == 1 and sexo == 'm':
        maior = idade
        velho = nome
    if sexo == 'm' and idade > maior:
        maior = idade
        velho = nome
    if sexo == 'm':
        ma += 1
    elif sexo == 'f':
        fe += 1
print('=-' * 30)
print('Neste grupo existem {} homens e {} mulheres.'.format(ma, fe))
print('A idade mais alta dos homens é {} e ele chama-se {}.'.format(maior, velho))
print('Neste grupo existem {} mulheres com menos de 20 anos de idade.'.format(x))
print('A media de todas as idades é de {:.0f} anos'.format(media))
