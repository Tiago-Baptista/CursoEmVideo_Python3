print('Calcule o seu amumento anual!')
salario = float(input('Qual o seu salário? €'))
if salario > 1250:
    aumento = salario + (salario * 10) / 100
    print('O seu salario é de {:.2f}€ terá um aumento de 10% e passará para {:.2f}€'.format(salario, aumento))
else:
    aumento = salario + (salario * 15) / 100
    print('O seu salario é de {:.2f}€ terá um aumento de 15% e passará para {:.2f}€'.format(salario, aumento))
