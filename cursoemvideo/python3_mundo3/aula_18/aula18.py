'''teste = list()
teste.append('Tiago')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 23
galera.append(teste[:])
print(galera)'''

'''galera = [['João', 19], ['Ana', 33], ['Maria', 45]]
#print(galera[0][0])
#print(galera[1][1])
for p in galera:
    #print(p)
    print(p[0])
    print(p[1])'''

galera = list()
dado = list()
tmaior = tmenor = 0
for c in range(0, 4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        tmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        tmenor += 1
print(f'Temos {tmaior} maiores e {tmenor} menores de idade.')
