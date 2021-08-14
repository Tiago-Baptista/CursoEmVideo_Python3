soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1 # é a mesma coisa que (cont = cont + 1)
        soma += c # e'a mesma coisa que (soma = soma + c)
print('A soma de todos os {} numeros solicitados é de {}'.format(cont, soma))
