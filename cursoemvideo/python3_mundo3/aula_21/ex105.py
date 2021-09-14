def notas(*n, sit=False):
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Media'] = sum(n)/len(n)
    if sit:
        if r['Media'] >= 7:
            r['Situação'] = 'Boa'
        elif r['Media'] >=5:
            r['Situação'] = 'Razoavel'
        else:
            r['Situação'] = 'Ruim'

    return r


#Programa Principal
resp = notas(5.5, 3.5, 9, 8, sit=True)
print(resp)
