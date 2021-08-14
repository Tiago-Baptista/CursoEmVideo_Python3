peso = float(input('Qual o seu peso(Kg)? '))
altura = float(input('Qual a sua altura(m)? '))
imc = peso / (altura * altura)
print('O seu IMC é de {:.1f}. '.format(imc), end='')
if imc < 18.5:
    print('Voce está abaixo do peso.')
elif 25 > imc >= 18.5:
    print('Voce está com o peso ideal!')
elif 30 > imc >= 25:
    print('Voce está com sobrepeso!')
elif 40 > imc >= 30:
    print('Voce está obeso!')
else:
    print('Voce tem obesidade morbida!!!')
