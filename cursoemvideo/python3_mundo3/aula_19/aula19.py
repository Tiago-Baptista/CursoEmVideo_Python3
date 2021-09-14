#pessoas = {'nome': 'Tiago', 'sexo': 'M', 'idade': 40}
'''print(pessoas['nome'])
print(pessoas['sexo'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())'''

'''#for k in pessoas.keys():
 #   print(k)
#for k in pessoas.values():
#    print(k)
#del pessoas['sexo']   #apagar elemento
#pessoas['nome'] = 'Rute'   #mudar elemento
pessoas['peso'] = 102   #adicionar elemento
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

'''brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' - ')
    print()
